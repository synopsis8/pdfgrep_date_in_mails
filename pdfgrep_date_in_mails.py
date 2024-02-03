#!/usr/bin/env python
# pdfgrep_date_in_mails.py
# Source : https://github.com/synopsis8/

import sys
import PyPDF2
import re

def pdfgrep_weekday_and_month(pdf_path, weekdays_matrix, months_matrix, num_occurrences=None):
    matching_lines = []

    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        for page_number in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_number)
            text = page.extract_text()

            for line_number, line in enumerate(text.split('\n'), start=1):
                for weekdays in weekdays_matrix:
                    for months in months_matrix:
                        for weekday in weekdays:
                            for month in months:
                                pattern = re.compile(f"{weekday.lower()}.*{month.lower()}", re.IGNORECASE | re.UNICODE)
                                matches = pattern.findall(line)
                                for match in matches:
                                    matching_lines.append((page_number, line_number, match))
                                    print(f"Page {page_number + 1}, Line {line_number}, Match: {match}, Full Line: {line}")

                                    if num_occurrences is not None and len(matching_lines) >= num_occurrences:
                                        return matching_lines

    return matching_lines

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python highlightdate.py <pdf_file> [num_occurrences]")
        sys.exit(1)

    pdf_file_path = sys.argv[1]
    num_occurrences = int(sys.argv[2]) if len(sys.argv) > 2 else None

    # Replace with the matrices you need (full names and abbreviations)
    weekdays_matrix_to_search = [
        ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
        ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"],
        ["Lu", "Ma", "Me", "Je", "Ve", "Sa", "Di"],
        ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"],
        ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"],
        ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"],
        ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    ]

    months_matrix_to_search = [
        ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
        ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"],
        ["Jan", "Feb", "Mär", "Apr", "Mai", "Jun", "Jul", "Aug", "Sep", "Okt", "Nov", "Dez"],
        ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"],
        ["Jan", "Feb", "Mär", "Apr", "Mai", "Jun", "Jul", "Aug", "Sep", "Okt", "Nov", "Dez"],
        ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"],
        ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
    ]

    matching_lines = pdfgrep_weekday_and_month(pdf_file_path, weekdays_matrix_to_search, months_matrix_to_search, num_occurrences)

    if not matching_lines:
        print("No matches found.")

