# RSS subscriptions

- Main articles: https://md.eknath.dev/index.xml
- All posts, including nested folders: https://md.eknath.dev/posts/index.xml
- Resources: https://md.eknath.dev/resources/index.xml

Home and section feeds include full rendered HTML in `content:encoded` and summaries in `description`. RSS is linked from the menu and advertised to feed readers. Search and Archives are excluded. Production builds omit drafts and future posts.

`params.rssSections: ["posts"]` limits only the main feed to articles. `services.rss.limit: -1` keeps all published items; set a positive value to limit each feed after filtering and sorting. JSON search output remains enabled.

`layouts/_default/rss.xml` is a generated project override from `shared/hugo/rss.xml` in EK Command Center. Edit the parent source and run `npm run theme:sync`; do not edit PaperMod's RSS template. `layouts/partials/extend_head.html` advertises the main feed on article pages; PaperMod supplies discovery on list pages.

Local and workflow-pinned Hugo builds plus XML regression checks should pass before publishing.
