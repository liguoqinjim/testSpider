# coding:utf8

from lxml import etree

xml = '''
<linedetails>
  <linedetail>
    <end_earlytime>05:30</end_earlytime>
    <end_latetime>22:45</end_latetime>
    <end_stop>锦西路打虎山路</end_stop>
    <line_id>10407</line_id>
    <line_name>871路</line_name>
    <start_earlytime>05:30</start_earlytime>
    <start_latetime>22:30</start_latetime>
    <start_stop>西营路成山路</start_stop>
  </linedetail>
</linedetails>
'''


def parse_xml():
    root = etree.fromstring(xml)
    #print root

    start_time1 = root.xpath('linedetail/end_earlytime/text()')
    print start_time1[0]




parse_xml()
