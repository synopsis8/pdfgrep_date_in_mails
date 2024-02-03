# pdfgrep_date_in_mails

A python program to highlight dates in PDF Email outputs

This Python script serves the purpose of extracting dates within an PDF document, i.e en Email.
Imagine you need to print out E-mails massively from your Inbox into PDF files and order those PDF files chronologically.
The dates will be one major criteria of choice for your needs.

Depending the mail provide you are using, the formating of the PDF output will vary significantly.
The script will match lines containing both "weekdays" and "month" as a valid match to be retained, this in order
to filter out unwanted common entries of weekdays or month in a conversation.

Optionnaly, you might want to restrict the number of occurences being displayed. This is achieved entering [num_occurrences] as parameter.

Usage: python pdfgrep_date_in_mails.py <pdf_file> [num_occurrences]

Development roadmap / new functionalities to be added:
- Date formating according [Date and time format reference - strftime](https://www.ibm.com/docs/en/workload-automation/10.2.1?topic=troubleshooting-date-time-format-reference-strftime)
- File renaming

Stay tuned
