Project Specification Feedback
==================

Commit graded: 41d99de60a304a087c70cfbcaec66e9474560aab

### The product backlog (10/10)

- Spreadsheet-like format is easier to read for backlogs. You can explore existing online tools for generating and tracking work on a project.
- What are time estimates for each task? If one task requires more than 5 hours, you should break into subtasks.
- First three feature may take a long time to make it complete. Focus on making those complete first, and `The Shop` feature could be implemented when if you have time.

### Data models (7/10)

- Please have some description of each models (and important fields).
- Page: `path` may be more appropriate name than `url` since `base_url` is already specified.
- Section: FYI, ArrayField is only supported in postgres.
- Customer: Customer should be OneToOne field to user.
- Customer: If you have `shop` as ForeignKey, would customer be able to shop in multiple shops? Why does customer be bind to shop in the first place?
- Customer: How is shopping cart implemented?
- Order: shouldn't `shop_id` just be ForeignKey to Shop?
- Order: `total price` could be defined as static method that loops through `products` instead of independent field to avoid any inconsistency.
- How is analytics implemented?
- Where is delivery address stored in the database? Can user have multiple delivery addresses?
- Where is Template Categories stored?

### Wireframes or mock-ups (10/10)

- Why is there two login pages? You should just submit only the final version.

### Additional Information

---
#### Total score (27/30)
---
Graded by: Sean D Kim (sdk1)

To view this file with formatting, visit the following page: https://github.com/CMU-Web-Application-Development/Team27/blob/master/feedback/specification-feedback.md
