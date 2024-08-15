Interview

At X, we manage law firms' clients, matters, and time entries. Lawyers work on different matters for various clients and bill their time accordingly.

For example, an attorney may be working on the Dropbox Inc. client, on their Series C Financing matter. And a time entry pertaining to that client-matter will describe the attorney's work and the duration of that work.

Each client can have one or more matters. And each time entry pertains to exactly one matter. In other words, the mapping of clients to matters is one-to-many. And the mapping of matters to time entries is one-to-many.
Client. Attributes:

Name (i.e. Dropbox Inc.)
Display number (i.e. C002)
Matter. Pertains to a single client. Attributes:

Name (i.e. Series C Financing)
Display number (i.e. M0004)
Time Entry. Pertains to a single matter. Attributes:

Narrative
Hours worked
Date


Objective
Design and implement a system that stores clients, matters, and time entries.
Implement methods to add new clients, matters, and time entries. Implement data validation to ensure each client has a unique display number, and each matter has a unique display number on a per-client basis. Note: Time entries can have hours that are not rounded floats.

Implement a method to retrieve the total number of hours across all time entries within a given matter