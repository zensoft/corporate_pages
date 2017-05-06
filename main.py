from i18n import I18N
import settings
import psycopg2
import os


def delete_file(path):
    try:
        os.remove(path)
    except OSError:
        pass


def clean_html(result_html):
    lines = result_html.split("\n")
    res = [s for s in lines if "<header>" not in s and "main-nav-check" not in s]
    return "\n".join(res)


def get_file_content_body(path):
    content = None
    with open(path) as f:
        content = f.read()
    return content


def get_file_content(path):
    with open(path, "r") as f:
        for l in f:
            yield l.strip()


def clear_all_but_not_root(conn):
    sql = "DELETE FROM corporate.corporate_page WHERE id > 0"
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    cur.close()


def get_content_body(country, page):
    file_path = settings.FRONT_VIEWS_PATH + country + "/" + page + settings.HTML_SUFFIX
    reading = False
    data = []
    for l in get_file_content(file_path):
        if "<!--START-->" in l:
            reading = True
            continue

        if "<!--END-->" in l:
            reading = False

        if reading:
            data.append(l + "\n")

    return "".join(data)


def get_css_content(page):
    css_path = settings.CRITICAL_CSS_PATH + page + settings.CSS_SUFFIX
    data = "\n".join([l for l in get_file_content(css_path)])
    return data


def parse_country(country, conn):
    sql_file = settings.OUT_SQL_PATH + country + settings.SQL_SUFFIX
    delete_file(sql_file)
    views = settings.VIEWS
    cur = conn.cursor()
    for item in views:
        page = item
        data_page = views[page]

        print("process -> {0}".format(page))

        content_body = get_content_body(country, page)

        css_content = get_css_content(page)

        id = data_page["id"]
        display_order = data_page["id"]
        parent_id = data_page["parent_id"]
        page_name = data_page["name"]

        friendly_url = data_page["friendly_url"]
        page_path_ids = data_page["page_path_ids"]

        sql = """
        INSERT INTO corporate.corporate_page
        (id, display_order, parent_id, page_name, friendly_url, published, corporate_page_type, html_content, root_page_id, page_path_ids, critical_css)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
        """

        res_sql = cur.mogrify(sql, (id, display_order, parent_id, page_name, friendly_url, True, 1 if id == 1 else 2, content_body, 1, page_path_ids, css_content))
        with open(sql_file, "a+") as f:
            sql_file_data = []
            sql_file_data.append("\n")
            sql_file_data.append("-- FILE " + page + "\n")
            sql_file_data.append(res_sql.decode("utf8").strip()+ "\n")
            f.write("".join(sql_file_data))

        # cur.execute(sql,
        #             (id, display_order, parent_id, page_name, friendly_url, True, 1 if id == 1 else 2, content_body, 1,
        #              page_path_ids, css_content)
        #             )
        # conn.commit()

        #print("==============")
        #break
    cur.close()


def main():
    conn = psycopg2.connect(database=settings.DATABASE,
                            user=settings.USER,
                            password=settings.PASS,
                            host=settings.HOST,
                            port=settings.PORT)
    #clear_all_but_not_root(conn)
    parse_country("pl", conn)
    conn.close()


if __name__ == "__main__":
    main()
