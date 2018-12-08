import scrapy


class TceCeSetSpider(scrapy.Spider):
  name = "tce_ce_spider"
  start_urls = ['https://www.tce.ce.gov.br:8082/portal/paginas/informacoes-funcionais.xhtml']

  def parse(self, response):
    SET_SELECTOR = '#form:categoriaFuncional'
    for pessoal in response.css(SET_SELECTOR):
      NAME_SELECTOR = 'option ::text'
#      PIECES_SELECTOR = './/dl[dt/text() = "Pieces"]/dd/a/text()'
#      MINIFIGS_SELECTOR = './/dl[dt/text() = "Minifigs"]/dd[2]/a/text()'
#      IMAGE_SELECTOR = 'img ::attr(src)'

      yield {
        'name': pessoal.css(NAME_SELECTOR).extract_first(),
#        'pieces': brickset.xpath(PIECES_SELECTOR).extract_first(),
#        'minifigs': brickset.xpath(MINIFIGS_SELECTOR).extract_first(),
#        'image': brickset.css(IMAGE_SELECTOR).extract_first(),
      }


#    NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
#    next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
#    if next_page:
#      yield scrapy.Request(
#      response.urljoin(next_page),
#      callback=self.parse
#    )






