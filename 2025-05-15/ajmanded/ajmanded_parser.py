def parser(url, page):
    try:
        page.goto(url)
        print(f"Opened URL: {url}")

        li_xpath = "//li[@class='res-item'][span[text()='License Number']]"
        page.wait_for_selector(li_xpath, timeout=10000)

        license_number = page.locator(li_xpath).evaluate(
            "node => node.childNodes[1].textContent.trim()"
        )
        license_type = page.locator("//li[@class='res-item'][span[text()='License Type']]").evaluate("node => node.childNodes[1].textContent.trim()")
        legal_form = page.locator("//li[@class='res-item'][span[text()='Legal Form']]").evaluate("node => node.childNodes[1].textContent.trim()")
        arabic_trade_name = page.locator("//li[@class='res-item'][span[text()='Arabic Trade Name']]").evaluate("node => node.childNodes[1].textContent.trim()")
        english_trade_name = page.locator("//li[@class='res-item'][span[text()='English Trade Name']]").evaluate("node => node.childNodes[1].textContent.trim()")
        license_start_date = page.locator("//li[@class='res-item'][span[text()='License Start Date']]").evaluate("node => node.childNodes[1].textContent.trim()")
        license_expiry_date = page.locator("//li[@class='res-item'][span[text()='License Expiry Date']]").evaluate("node => node.childNodes[1].textContent.trim()")

        activities = page.locator("//div[@class='result mt-4'][h5[text()='Activities']]//li[@class='res-item']")
        activities = [activities.nth(i).inner_text() for i in range(activities.count())]

        if page.locator("//li[@class='res-item'][span[text()='Establishment Banning Status']]").count() > 0:
            banning_status_raw = page.locator("//li[@class='res-item'][span[text()='Establishment Banning Status']]").text_content()
            banning_status = banning_status_raw.replace("Establishment Banning Status", "").strip()
        else:
            banning_status = None

        if page.locator("//li[@class='res-item'][span[text()='Establishment Banning Reason']]").count() > 0:
            banning_reason_raw = page.locator("//li[@class='res-item'][span[text()='Establishment Banning Reason']]").text_content()
            banning_reason = banning_reason_raw.replace("Establishment Banning Reason", "").strip()
        else:
            banning_reason = None

        if page.locator("//li[@class='res-item'][span[text()='Area']]").count() > 0:
            area_raw = page.locator("//li[@class='res-item'][span[text()='Area']]").text_content()
            area = area_raw.replace("Area", "").strip()
        else:
            area = None

        if page.locator("//li[@class='res-item'][span[text()='Pelvis Number']]").count() > 0:
            pelvis_number_raw = page.locator("//li[@class='res-item'][span[text()='Pelvis Number']]").text_content()
            pelvis_number = pelvis_number_raw.replace("Pelvis Number", "").strip()
        else:
            pelvis_number = None

        if page.locator("//li[@class='res-item'][span[text()='Block Number']]").count() > 0:
            block_number_raw = page.locator("//li[@class='res-item'][span[text()='Block Number']]").text_content()
            block_number = block_number_raw.replace("Block Number", "").strip()
        else:
            block_number = None

        if page.locator("//li[@class='res-item'][span[text()='Unit Type']]").count() > 0:
            unit_type_raw = page.locator("//li[@class='res-item'][span[text()='Unit Type']]").text_content()
            unit_type = unit_type_raw.replace("Unit Type", "").strip()
        else:
            unit_type = None

        if page.locator("//li[@class='res-item'][span[text()='Unit Number']]").count() > 0:
            unit_number_raw = page.locator("//li[@class='res-item'][span[text()='Unit Number']]").text_content()
            unit_number = unit_number_raw.replace("Unit Number", "").strip()
        else:
            unit_number = None

        if page.locator("//li[@class='res-item'][span[text()='Makani Number']]").count() > 0:
            makani_number_raw = page.locator("//li[@class='res-item'][span[text()='Makani Number']]").text_content()
            makani_number = makani_number_raw.replace("Makani Number", "").strip()
        else:
            makani_number = None
        

    except Exception as e:
        print("Failed to extract license number:", e)
        return None
