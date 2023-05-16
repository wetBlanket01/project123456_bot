from yoomoney import Authorize

Authorize(
    client_id="41FB49EBCDE105B7DCAA74A6AC62257E35A48F101B4DEAA2D7F71C1DCCD14DC0",
    redirect_uri="http://t.me/cyberSportikBot",
    scope=["account-info",
           "operation-history",
           "operation-details",
           "incoming-transfers",
           "payment-p2p",
           "payment-shop",
           ]
    )
