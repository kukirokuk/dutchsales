from openprocurement.auctions.dutchsales.models import DGFOtherAssets, DGFFinancialAssets


def includeme(config):
    config.add_auction_procurementMethodType(DGFOtherAssets)
    config.scan("openprocurement.auctions.dutchsales.views.other")

    config.add_auction_procurementMethodType(DGFFinancialAssets)
    config.scan("openprocurement.auctions.dutchsales.views.financial")
