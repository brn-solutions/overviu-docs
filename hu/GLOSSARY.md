# Overviu Hungarian glossary

One Hungarian term per concept, used the same way in the app (`lang/hu.json` in the overviu repo) and in these docs.
The terms come from the app's translation; when a term changes, change it in `hu.json` first, then here and in the
`hu/` pages.

## Register

Formal "Ön" everywhere: the host app, the booking site, every email and the docs. Never "te" (no "fiókod",
"Válaszd", "Kattints").

## Formats

| What | English | Hungarian |
|---|---|---|
| Date | 15 October 2026 | 2026. október 15. |
| Short date | 15 Oct | okt. 15. |
| Stay | 14–18 Oct | okt. 14–18. |
| Forint | HUF 12,000 | 12 000 Ft |
| Euro | €1,200.50 | 1 200,50 EUR |
| Weekday | Monday | Hétfő |

Hungarian money uses a space between thousands, a decimal comma and the currency after the amount. Whole amounts have
no decimals.

## Places and listings

| English | Hungarian | Note |
|---|---|---|
| listing | szálláshirdetés | What the host manages in **Szálláshirdetések**. |
| place to stay | szálláshely | What the guest looks for and books. |
| property | ingatlan | |
| single property | önálló ingatlan | |
| building | épület | |
| whole building | teljes épület | |
| unit type | egységtípus | |
| unit | egység | |
| property type | ingatlan típusa | |
| amenities | felszereltség | |

## Bookings and guests

| English | Hungarian | Note |
|---|---|---|
| booking | foglalás | |
| booking code | foglalási kód | |
| guest | vendég | |
| host | szállásadó | |
| stay | tartózkodás | |
| check-in | bejelentkezés | Also the word for signing in. See "Open questions". |
| check-out | kijelentkezés | Also the word for signing out. |
| online check-in | online bejelentkezés | |
| changeover | vendégváltás | Also used for "turnover". |
| guest page | vendégoldal | |
| booking page | foglalási oldal | The guest's private page for one booking. |
| booking site | foglalási weboldal | The host's own site guests book on. |
| arrival pack | érkezési információs csomag | |
| rental agreement | bérleti szerződés | |
| booking terms | foglalási feltételek | |
| cancellation policy | lemondási szabályzat | |
| inbox | beérkezett üzenetek | |
| coupon | kupon | |

## Booking and listing statuses

| English | Hungarian |
|---|---|
| Pending | Függőben |
| Awaiting payment | Fizetésre vár |
| Confirmed | Visszaigazolva |
| Cancelled | Lemondva |
| Completed | Befejezve |
| Paid | Fizetve |
| Part paid | Részösszeg fizetve |
| Pay at check-in | Fizetés érkezéskor |
| Draft | Piszkozat |
| Active | Aktív |
| Archived | Archiválva |

## Money

| English | Hungarian | Note |
|---|---|---|
| payment | fizetés | |
| checkout (Stripe's payment page) | fizetés, fizetési oldal | Not check-out. |
| part payment | részfizetés | |
| balance | egyenleg | |
| security deposit | kaució | |
| refundable deposit | visszatéríthető kaució | |
| refund | visszatérítés | |
| extra charge | pótdíj | |
| tourist tax | idegenforgalmi adó | |
| nightly rate | éjszakánkénti ár | |
| seasonal rules | szezonális szabályok | |
| occupancy | kihasználtság | |
| revenue | bevétel | |
| net income | nettó bevétel | |
| money in / money out | bevételek / kiadások | |

## Team and plan

| English | Hungarian |
|---|---|
| team | csapat |
| team members | csapattagok |
| Owner | Tulajdonos |
| Admin | Adminisztrátor |
| Member | Tag |
| plan | előfizetés |
| Plan & billing | Előfizetés és számlázás |
| free trial | ingyenes próbaidőszak |
| Monthly / Yearly | Havi / Éves |
| Enterprise | Vállalati |
| paused (team) | szüneteltetve |

## App areas

| English | Hungarian |
|---|---|
| Dashboard | Műszerfal |
| Calendar | Naptár |
| Bookings | Foglalások |
| Inbox | Beérkezett üzenetek |
| Listings | Szálláshirdetések |
| Reports | Jelentések |
| Settings | Beállítások |
| Branding | Arculat |
| Help & guides | Súgó és útmutatók |
| Ask Overviu | Kérdezze az Overviut |

## Kept in English

Brand and technical names stay as they are: Airbnb, Booking.com, Vrbo, Expedia, Stripe, OpenAI, Claude, Wi-Fi, AI,
CNAME, Webhook, domain.

## Open questions

- **Check-in and sign-in share a word.** "Bejelentkezés" means both checking in to a stay and signing in to an account,
  and "Kijelentkezés" means both check-out and signing out. Booking.com's Hungarian site uses "Bejelentkezés" for
  check-in and "Belépés" for signing in. Moving sign-in to "Belépés" and "Kilépés" would remove the clash.
