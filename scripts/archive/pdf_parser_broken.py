"""
BSE Orders
Module: PDF Parser
Version: 1.0.0
Status: Sprint-1 Foundation
"""
from pathlib import Path
import json
import re

RAW_FOLDER = Path("data/raw")

class PDFParser:
    def __init__(self):
        self.reset()

    def reset(self):
        self.fields = {
            "company": "",
            "announcement_date": "",
            "awarding_entity": "",
            "order_value": "",
            "execution_period": "",
            "order_type": "",
            "domestic": "",
            "project_description": "",
            "source_file": ""
        }

    def normalize_text(self, text):
        return "\n".join([l.strip() for l in text.replace("\r","").split("\n") if l.strip()])

    def load_file(self, txt_file):
        self.reset()
        self.fields["source_file"] = txt_file.name
        return self.normalize_text(txt_file.read_text(encoding="utf-8", errors="ignore"))

    def clean(self, value):
        return re.sub(r"\s+"," ",value).strip(" :;,-")

    def find_after_label(self,text,labels):
        lines=text.split("\n")
        for i,line in enumerate(lines):
            low=line.lower()
            for label in labels:
                if label.lower() in low:
                    part=self.clean(line[low.find(label.lower())+len(label):])
                    if part:
                        return part
                    for nxt in lines[i+1:i+6]:
                        nxt=self.clean(nxt)
                        if len(nxt)>2:
                            return nxt
        return ""

    def extract_company(self,text):
        pats=[
            r"For\s*&\s*on\s*behalf\s*of\s+([A-Za-z0-9&.,()'\/\- ]+?(?:Limited|Ltd\.?))",
            r"For\s+([A-Za-z0-9&.,()'\/\- ]+?(?:Limited|Ltd\.?))"
        ]
        for p in pats:
            m=re.search(p,text,re.I)
            if m:
                self.fields["company"]=self.clean(m.group(1)); return

    def extract_date(self,text):
        for p in [
            r"Date\s*[:\-]?\s*(\d{2}\.\d{2}\.\d{4})",
            r"Date\s*[:\-]?\s*([A-Za-z]+\s+\d{1,2},\s+\d{4})",
            r"Date\s*[:\-]?\s*(\d{2}-\d{2}-\d{4})"]:
            m=re.search(p,text,re.I)
            if m:
                self.fields["announcement_date"]=self.clean(m.group(1)); return

def extract_order_value(self, text):

    patterns = [
        r"Broad consideration.*?(INR\s*₹?[\d,]+(?:\.\d+)?\s*(?:Crore|Crores|Lakh|Lakhs)?)",
        r"Work Order Value.*?(₹\s*[\d,]+(?:\.\d+)?\s*(?:Crore|Crores|Lakh|Lakhs)?)",
        r"Work Order Value.*?(Rs\.?\s*[\d,.]+\s*(?:Crore|Crores|Lakh|Lakhs)?)",
        r"Total estimated value.*?(INR\s*[\d,.]+\s*(?:Crore|Crores|Lakh|Lakhs)?)",
        r"estimated value.*?(INR\s*[\d,.]+\s*(?:Crore|Crores|Lakh|Lakhs)?)",
        r"total value.*?(₹\s*[\d,]+(?:\.\d+)?)",
        r"contract is\s*(₹\s*[\d,]+(?:\.\d+)?)",
        r"approximately\s*(INR\s*[\d,.]+\s*(?:Crore|Crores|Lakh|Lakhs)?)",
        r"~\s*(INR\s*[\d,.]+\s*(?:Crore|Crores|Lakh|Lakhs)?)"
    ]

    for pattern in patterns:

        m = re.search(
            pattern,
            text,
            re.IGNORECASE | re.DOTALL
        )

        if m:

            value = re.sub(r"\s+", " ", m.group(1))

            self.fields["order_value"] = value.strip()

            return


def extract_awarding_entity(self, text):
        
        self.fields["awarding_entity"]=self.find_after_label(text,[
            "Name of the entity awarding the",
            "name of the entity awarding the",
            "Name of the entity awarding",
            "name of the entity awarding"
        ]
        )

    def parse(self, txt_file):

    t = self.load_file(txt_file)

    self.extract_company(t)

    self.extract_date(t)

    self.extract_order_value(t)

    self.extract_awarding_entity(t)

    return self.fields

def main():
    p=PDFParser()
    files=sorted(RAW_FOLDER.glob("*.txt"))
    print(f"Found {len(files)} TXT files")
    for f in files:
        print("="*80)
        print(json.dumps(p.parse(f),indent=4,ensure_ascii=False))

if __name__=="__main__":
    main()
