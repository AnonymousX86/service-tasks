# Service Tasks

GUI app for managing service tasks. Both for customers and for service 
providers.

## Customer

### Main page

List with all commissions. Customer can click on each commission to see the 
details.

### Commission details

- Name
- Description
- Date (created)
- Photo preview

### Contact

Contact form for creating a new commission.

## Service Provider

### Main page

Same as for client, but with additional button for quick creating new commission.
Also, the commissions details provide customer info.

### Commission details

Same as for client. Additional info about the client.

### Contact

Inbox with all messages from the client.

## Database structure

Every service provider has its own entry. With ID, name, email, phone,
and password.
Every task has its own entry. With ID, name, description, date, photo. It's 
linked to the service provider and the client.
Task's client can see the details about the service provider.
