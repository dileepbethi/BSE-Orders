[1mdiff --git a/scripts/scraper.py b/scripts/scraper.py[m
[1mindex f52aca2..efdf156 100644[m
[1m--- a/scripts/scraper.py[m
[1m+++ b/scripts/scraper.py[m
[36m@@ -7,18 +7,22 @@[m [mfrom parser import get_result_rows[m
 from downloader import download_pdf[m
 [m
 [m
[31m-def open_bse([m
[31m-    from_date,[m
[31m-    to_date[m
[31m-):[m
[32m+[m[32mdef open_bse(from_date, to_date):[m
 [m
     download_folder = Path("data/downloads")[m
     download_folder.mkdir(parents=True, exist_ok=True)[m
 [m
[32m+[m[32m    downloaded_files = [][m
[32m+[m
     with sync_playwright() as p:[m
 [m
         browser = p.chromium.launch([m
             headless=False[m
[32m+[m[32m            args=[[m
[32m+[m[32m                "--disable-gpu",[m
[32m+[m[32m                "--disable-dev-shm-usage",[m
[32m+[m[32m                "--no-sandbox",[m
[32m+[m[32m            ][m
         )[m
 [m
         context = browser.new_context([m
[36m@@ -34,16 +38,44 @@[m [mdef open_bse([m
             wait_until="domcontentloaded",[m
             timeout=60000[m
         )[m
[32m+[m[32m        page.wait_for_timeout(5000)[m
[32m+[m
[32m+[m[32m        print("\nCurrent URL:")[m
[32m+[m[32m        print(page.url)[m
[32m+[m
[32m+[m[32m        print("\nTitle:")[m
[32m+[m[32m        print(page.title())[m
[32m+[m
[32m+[m[32m        page.screenshot([m
[32m+[m[32m            path="page_debug.png",[m
[32m+[m[32m            full_page=True[m
[32m+[m[32m   )[m
[32m+[m
[32m+[m[32m        print("\nScreenshot saved as page_debug.png")[m
[32m+[m
[32m+[m[32m        print("[INFO] Waiting for Angular page...")[m
 [m
[31m-        page.wait_for_timeout(3000)[m
[32m+[m[32m        page.wait_for_timeout(5000)[m
[32m+[m
[32m+[m[32m        page.wait_for_load_state("domcontentloaded")[m
[32m+[m
[32m+[m[32m        print("[INFO] Current URL:", page.url)[m
[32m+[m
[32m+[m[32m        print("[INFO] ddlAnnType count:",[m
[32m+[m[32m              page.locator("#ddlAnnType").count())[m
[32m+[m
[32m+[m[32m        page.wait_for_selector([m
[32m+[m[32m            "#ddlAnnType",[m
[32m+[m[32m            timeout=30000[m
[32m+[m[32m        )[m
 [m
         print("[INFO] Applying Filters...")[m
 [m
         apply_filters([m
[31m-     page,[m
[31m-    from_date,[m
[31m-    to_date[m
[31m-)[m
[32m+[m[32m            page,[m
[32m+[m[32m            from_date,[m
[32m+[m[32m            to_date[m
[32m+[m[32m        )[m
 [m
         records = get_result_rows(page)[m
 [m
[36m@@ -60,7 +92,6 @@[m [mdef open_bse([m
 [m
             success = 0[m
             failed = 0[m
[31m-            downloaded_files = [][m
 [m
             for i, record in enumerate(records, start=1):[m
 [m
[36m@@ -94,40 +125,31 @@[m [mdef open_bse([m
                     except Exception as e:[m
 [m
                         failed += 1[m
[31m-[m
                         print(f"[ERROR] {e}")[m
 [m
                 else:[m
 [m
                     failed += 1[m
[31m-[m
                     print("[WARNING] No PDF link found.")[m
 [m
             print("\n" + "=" * 80)[m
[31m-[m
             print("DOWNLOAD SUMMARY")[m
[31m-[m
             print(f"Total Records : {len(records)}")[m
             print(f"Downloaded    : {success}")[m
             print(f"Failed        : {failed}")[m
[31m-[m
             print("=" * 80)[m
 [m
         input("\nPress Enter to close browser...")[m
 [m
         context.close()[m
[31m-[m
         browser.close()[m
 [m
[31m-        return downloaded_files[m
[32m+[m[32m    return downloaded_files[m
 [m
 [m
 if __name__ == "__main__":[m
 [m
     open_bse([m
[31m-[m
         "14-07-2026",[m
[31m-[m
         "14-07-2026"[m
[31m-[m
     )[m
\ No newline at end of file[m
