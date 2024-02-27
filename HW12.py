import pandas as pd
import numpy as np
url = "https://datascience.quantecon.org/assets/data/wdi_data.csv"
df = pd.read_csv(url)
#df.info()

df_year = df.set_index(["year"])

#เพิ่ม column net export และ investment
nx = df_year["Exports"] - df_year["Imports"]
df_year["NetExports"] = nx
df_year["Investment"] = df_year.eval("GDP - Consumption - GovExpend - NetExports")

#1) ใช้ .loc กับ .iloc
rec_year2001 = df_year.loc[2001,["country", "Exports", "Imports", "Investment"]] #ดูข้อมูลที่เป็นปี 2001 โดยแสดง country exports imports investment
rec_from_index34 = [34, [3,4,7]]

#2) ใข้คำสั่ง .loc สำหรับตัวแปร wdi ที่กำหนด index 2 ชั้น
wdi = df_year.reset_index()
wdi = wdi.set_index(["country" ,"year"])
print(wdi)