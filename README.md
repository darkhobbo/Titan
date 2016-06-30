# Titan

A recreation of https://github.com/chadfawcett/mailhound in Python using Flask. Once set up, the submitted form data will be sent to a mail provider like [Mailgun](https://mailgun.com) or [Sendgrid](https://sendgrid.com) and then forwarded to another email that can be specified in an environment variable.

For hosting I utilized Heroku.

## Environment Variables

ADMIN: yourname <email@mail.com>    e.g:  bob <bob@gmail.com><br>APIKEY: The apikey provided by Mailgun or Sendgrid for accessing their API.

## License

This software is free to use under the MIT license. See the [LICENSE][] file for more details.

[License]: https://github.com/darkhobbo/Titan/blob/master/LICENSE
