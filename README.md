# manymail
Ever had the need to send mails to multiple people but change only specific part of the email? Well, `manymail` is the solution.

## Example JSON POST Data
```
{
    "email_from": "some@gmail.com",
    "email_passw": "password123",
    "email_to": [
        {
            "email_to": "someemail@gmail.com",
            "email_change_data": ["data1,", "data2", ...]
        },
        ...
    ],
    "email_dynamic_fields": ["<<name>>", "<<address>>"],
    "email_subject": "This is test subject",
    "email_body": "This is my email body, <<name>> needs to be replaced for every recipient. The recipient's known address is <<address>>",
}
```