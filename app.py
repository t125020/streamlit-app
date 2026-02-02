import streamlit as st
import pandas as pd

st.title("林業産出額推移")
st.markdown("このサイトは林業に関する様々な要素の数十年分の産出額の推移を表示し、比較することができます。")
st.link_button("データの情報源はこちら","https://www.e-stat.go.jp/")
st.caption("単位は万円")

df = pd.read_csv("林業産出額.csv")

df['年'] = df["年"].astype(int)

for col in df.columns[1:]:
    df[col] = (
        df[col]
        .astype(str)
        .str.replace(",","")
        .str.strip()
        .astype(int)
    )

with st.sidebar:
    st.header("林業産出額分析サイト")
    st.image("林アイコン.png")
    branch = st.multiselect('項目を選択してください',["計","製材用素材等","輸出丸太","燃料用チップ素材","栽培キノコ類生産","薪炭生産","林野副産物採取","生産林業所得","木材生産"])

if branch:
    st.line_chart(df.set_index("年")[branch])

else:
    st.info("左のサイドバーから表示したい項目を選択してください。")    