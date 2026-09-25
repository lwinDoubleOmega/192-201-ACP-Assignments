# Assignment 03 — CHANGES

**Name:** Lwin Oo  **Student ID:** 6705140051

## 1 · What I changed

| # | Problem in the old code | What I changed | OOP concept | How I checked it |
|---|---|---|---|---|

| 1 | Products and order items were tuples, so it was hard to know what each index meant. | I made `Product` and `OrderItem` classes with clear attributes like name, price, category, and quantity. | Classes and composition | I checked the item totals and ran the self-test. |


| 2 | The old code did not check if the data was valid. | I added checks for empty names, negative prices, wrong product objects, quantities below one, and orders with no items. | Encapsulation and validation | I tested valid objects and invalid values. |


| 3 | Discount and points used many `if/elif` checks for the customer tier. | I made a base `Customer` class and subclasses for Silver, Gold, and Platinum. Each type has its own rates and points multiplier. | Inheritance and polymorphism | I checked the values for every customer type and tested all four orders. |


| 4 | The `calc()` function did calculations and printing in one large function. | I separated it into small methods for subtotal, quantity, discount, tax, total, points, and receipt printing. | Pure methods and separation of responsibilities | I compared every calculated result with the original output. |


| 5 | The old code had numbers such as `0.07`, `100`, and `10` directly inside the calculations. | I gave those values names such as `TAX_RATE`, `DISCOUNT_THRESHOLD`, and `POINTS_DIVISOR`. I also created the store data as objects in `refactored_main()`. | Clean code | I ran `python3 Assignment_03.py` and got PASS. |

## 2 · Short reflection

I think the customer subclasses improved the code the most. Before, the program checked the tier many times, but now each customer type stores its own discount rates and points multiplier. Splitting the calculations into small methods also made the program easier for me to follow and test. I had to be careful with the bulk discount because it is added when the total quantity is ten or more. I also learned that the output must match exactly, including rounding and blank lines. At the end, I ran the provided test and got PASS.

## 3 · Prompt log (Level 2)

| # | My prompt to the AI | What the AI helped with | What I did with it | How I checked it |
|---|---|---|---|---|
| 1 | “Let’s refactor the `calc` function and break it down piece by piece.” | It suggested separating the code into products, items, customers, orders, calculations, and printing. | I followed the structure and wrote it one part at a time. | I compared each part with the old `calc()` function. |


| 2 | “Check `Assignment_03.py`.” | It found missing validation, bulk discount logic, polymorphism, and `refactored_main()`. | I worked on the missing parts one by one. | I ran syntax checks and tested the calculations. |


| 3 | “Check again.” | It found that my conditional `raise` statements caused a `TypeError`. | I changed them to normal `if` statements. | I created valid objects and confirmed they worked. |


| 4 | “Again.” | It checked my constructors and `total_quantity()` method. | I kept `total_quantity()` and continued to the next part. | I tested ten Notebooks and got the correct 3% bulk discount. |


| 5 | “Finished.” | It checked `line_total()` and showed where I could reuse it. | I used it in subtotal, tax, and receipt printing. | I tested the calculations for all four orders. |


| 6 | “Done.” | It checked the customer subclasses and explained how they could replace the tier checks. | I added the customer discount and points methods. | I checked the rates and multiplier of each customer type. |


| 7 | “Done.” | It found that two customer methods had the wrong indentation and names. | I moved them inside `Customer` and changed the names to match their calls. | I ran the calculations again. |


| 8 | “Done.” | It found that the old tier checks were still inside `Order.points()`. | I replaced them with a call to the customer’s points method. | All four orders returned the expected results. |


| 9 | “Let’s do it one by one.” | It showed how to start `refactored_main()` with product and customer objects. | I created the objects using the original store data. | I used the provided self-test while working. |


| 10 | “Give me multiple steps and explanations.” | It explained how to create the orders, print receipts, add totals, and use a food tax constant. | I completed `refactored_main()` using those steps. | I ran the whole program. |


| 11 | “Do I fulfill the rubric points?” | It checked the rubric and found a spelling mistake in `FOOD_TAX_RATE`. | I corrected the spelling mistake. | The self-test printed PASS. |

**Ownership statement.** By submitting, I confirm that I understand and can explain every line of code I submitted, and that this prompt log shows how I used AI.

## 4 · Before-you-submit checklist

- [x] `python3 Assignment_03.py` prints **PASS**.
- [x] Products, orders, and items are objects.
- [x] Customer tiers use subclasses instead of `if tier == ...` chains.
- [x] Calculation methods return values, and receipt printing is separate.
- [x] Constructors check important values, and important numbers have names.
- [x] The change table and reflection are complete.
- [x] The prompt log and ownership statement are included.
