## What is a public connection?

A public connection is an OAuth connection that users install into their Notion workspaces. Unlike [internal connections](https://developers.notion.com/guides/get-started/internal-connections), which are scoped to a single workspace with a static token, public connections follow the [OAuth 2.0](https://oauth.net/2/) protocol: each user who authorizes the connection receives their own access token, scoped to their workspace.

When you create a public connection, you also choose its [installation scope](#installation-scope) — either **Any workspace** (Marketplace-eligible) or **Selected workspaces only** (not Marketplace-eligible).

If you only need a token for your own scripts, CLI workflows, Workers, or trusted tools, use a [personal access token](https://developers.notion.com/guides/get-started/personal-access-tokens). PATs also act as one Notion user, but they do not provide an OAuth install flow for other users.

This guide covers:

- How public connections differ from internal connections
- How installation scope controls who can install your connection
- How users authorize a public connection via OAuth
- How to create a public connection in the Developer portal

## How public connections differ from internal connections

The key differences come down to scope, identity, and how access is granted:

- **Scope:** Internal connections work in one workspace; public connections can install into many. [Installation scope](#installation-scope) controls which workspaces are eligible.
- **Identity:** Internal connections operate as their own bot user with permissions independent of any specific person. Public connections act on behalf of the individual user who authorized them — the access token is tied to that user. [Personal access tokens](https://developers.notion.com/guides/get-started/personal-access-tokens) are also tied to one user, but they are created directly by that user instead of through OAuth.
- **Page access:** Internal connections require workspace members to manually share pages via the “Add connections” menu. Public connections use the OAuth page picker, where users choose which pages to grant access to during the authorization flow.

For a full comparison, see the [comparison table](https://developers.notion.com/guides/get-started/overview#comparison) in the Overview.

## Installation scope

Every public connection has an **installation scope** that controls which workspaces can install it. You pick the scope when you create the connection.

| Scope | Who can install | Marketplace eligible |
| --- | --- | --- |
| Any workspace | Any Notion user, in any workspace. | Yes |
| Selected workspaces only | Only the workspaces you select at creation time. | No |

Installation scope is set once, at creation time, and can’t be changed afterward. If you pick **Selected workspaces only** and later want to list on the Marketplace, create a new connection.

## How users authorize a public connection

When a user wants to use your public connection, they go through an OAuth authorization flow:

Public connections can also offer a Notion template during the auth flow. If configured, users can choose to duplicate the template into their workspace instead of selecting existing pages. See the [Authorization guide](https://developers.notion.com/guides/get-started/authorization#prompt-for-a-connection-with-a-notion-template-option) for details on configuring templates.

After a user authorizes a public connection, only that user can interact with the connection in their workspace. If multiple members in a workspace want to use the same public connection, each user needs to complete the authorization flow individually.

## Creating a public connection

Marketplace listing details (such as descriptions, categories, and images) are managed separately through the **Listings** section. See [List on the Marketplace](https://developers.notion.com/guides/get-started/marketplace-listing) for details.

## Next steps

## Set up OAuth authorization

Implement the full OAuth 2.0 flow for your public connection.

## Preparing for users

Automate user onboarding after they install your connection.