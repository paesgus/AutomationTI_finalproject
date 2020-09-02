#!/usr/bin/env python3

import os
import datetime
import reports
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors


def generate_title():
  today = datetime.date.today().strftime("%B %d, %Y")
  return "Processed_Update on " + today

def generate_paragraph():
  path = os.getcwd() + '/supplier-data/descriptions/'
  report_content = ""

  for f in os.listdir(path):
    n, e = os.path.splitext(f)
    with open(os.path.join(path,f),  'r') as content:
      list = [x.strip() for x in content]
      name = 'name: ' + list[0]
      weight = 'weight: ' + list[1]
      report_content = report_content + name + '<br/>' + weight + '<br/><br/>'
  return report_content


def generate_report(attachment, title, paragraph):

  report = SimpleDocTemplate(attachment)
  styles = getSampleStyleSheet()
  report_title = Paragraph(title, styles["h1"])
  report_info = Paragraph(paragraph, styles["BodyText"])
  empty_line = Spacer(1,20)
  report.build([report_title, empty_line, report_info])


def main():
  reports.generate_report('/tmp/processed.pdf', generate_title(),generate_paragraph())
  print("Done!")

if __name__ == "__main__":
  main()
