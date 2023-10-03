# Dynatrace_Audit_Logs
This is a simple **Web page** designed and created to fetch Dynatrace Environment Audit Logs and to visualize them in Tabular format because Dynatrace does not provide us option to view Environment's Audit Logs on GUI.

We can fetch them using **Dynatrace's Audit Logs API**:

**API Documentation:** https://www.dynatrace.com/support/help/shortlink/api-audit-logs-get-log

**Authentication:**

To execute this request, you need an **access token** with **auditLogs.read** scope.

**Working:**

We have **2** files **Fetch_AuditLogs.html** & **Custom_http_server.py**.

Fetch_AuditLogs.html is our **Web Page** code file while Custom_http_server.py **hosts** our page on local machine in Windows.

![d574e9b8-2637-4de3-a60d-f4df280901b3](https://github.com/AdilSaleem98/Dynatrace_Audit_Logs/assets/47393539/bd622b47-61ce-4652-bf2c-fa859fafbcd3)


**Following are the features that this Web page provides:**
- We can select between **2 Environments** from dropdown option: I have labled them as **Environment1** & **Environment2** in this code that you can replace with your environments' names
  
  ![a1b87503-e6f5-45fc-ba2a-cf630497f664](https://github.com/AdilSaleem98/Dynatrace_Audit_Logs/assets/47393539/1e16f076-85e4-4474-9fdd-fed807218f7b)

- We can select the **timeframe** for which we want to get Logs from Dynatrace Cluster: you can add more presets in the **dropdown div**

  ![2801676c-0419-474f-ac32-7941f1bab406](https://github.com/AdilSaleem98/Dynatrace_Audit_Logs/assets/47393539/fa92ec7a-1baf-450c-acc0-571bc0629c0a)

- We can fetch **Logs of all event types** at once and we can get them **individually** by each event type

  ![e72d16f1-de43-47fd-b8a1-d73636c7625d](https://github.com/AdilSaleem98/Dynatrace_Audit_Logs/assets/47393539/6eb1e952-ee39-4724-8254-33c651ba96c3)     ![beb0a1fd-faed-4a95-ac60-61e2a109fa66](https://github.com/AdilSaleem98/Dynatrace_Audit_Logs/assets/47393539/e18fce4d-2d15-4221-98f3-151a1d4835a0)

- After fetching and displaying the Logs on screen, we can also **filter** and **search** data based on any value of any column of table

![22a2f286-614e-4321-91fd-827ddb1c983b](https://github.com/AdilSaleem98/Dynatrace_Audit_Logs/assets/47393539/d8e45786-ebf1-4faa-a372-4c2be2cba51a)


Currently, **"Fetch Audit Logs"** button on main page and **"SUMMARY"** button on the left tab doing the same task and fetching all logs at once.

**What changes are required in both the files to be able to execute them on your machine?**

- **Fetch_AuditLogs.html**
  - **Replace Environments' Names** and **IDs** with your actual data
  
    ![33505f6b-70f4-4c3c-bf69-5ec77ec74a31](https://github.com/AdilSaleem98/Dynatrace_Audit_Logs/assets/47393539/16c132a2-d939-4856-9e12-945c9dac7c6c)
  
    ![37e7e3b4-4310-49e8-bedf-140259911388](https://github.com/AdilSaleem98/Dynatrace_Audit_Logs/assets/47393539/217efa12-90f3-4acc-b0cf-6badcaf4031a)


  - **Write** your **Dynatrace Cluster URL**
  
    ![cf2b4dee-4035-4b14-966d-08ced3ecb541](https://github.com/AdilSaleem98/Dynatrace_Audit_Logs/assets/47393539/24103f0b-730a-4163-8564-be45810df009)

  - **Provice Access Tokens** with **auditLogs.read** scope for both of your environments

    ![98493256-b7f5-41a1-996b-bd49f032965b](https://github.com/AdilSaleem98/Dynatrace_Audit_Logs/assets/47393539/0b855602-c4f9-42c9-856f-d31b1882a492)


- **Custom_http_server.py**
  - **Dependencies:** **Python3**, **http** & **socketserver** modules
  - **Port 8000** is used in my case, **but** you can replace as per your choice
 
    ![6f233ccc-440f-4c27-bdfe-815c30a4186f](https://github.com/AdilSaleem98/Dynatrace_Audit_Logs/assets/47393539/9d9f441d-e9a2-4673-99b5-be96dcae0f6c)
    
  - **Write** your **machine's IPv4** where this page will be **hosted**
 
    ![2d505965-9ce1-44d4-909b-b5cb2e08c078](https://github.com/AdilSaleem98/Dynatrace_Audit_Logs/assets/47393539/32dd7359-ade1-46f4-a1e7-51125dfedd74)

**How to host and Access page?**

- **First**, you need to **place both files** in the **same folder** in your machine
- Open PowerShell, **cd** to the folder where both files are stored
- **Run** **"python Custom_http_server.py"** command and your page will be hosted on the selected port
- **Type** **"<Your_IP>:port/Fetch_AuditLogs.html"** in your browser and you will be able to see the page
- **Now**, you can fetch Audit Logs as per your requirement

**Note:** You can only access **"<Your_IP>:port/Fetch_AuditLogs.html"** as other URLs are restrited via code. You can also share mentioned URL with others: if they are in the same network as yours then they will be able to access this page
