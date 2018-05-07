import pandas as pd
import csv

def main():

    # Read csv file, delete duplicates and write it.
    with open('resultss.csv', 'r',newline='') as inputfile:
        with open('no_dupss_.csv', 'w', newline='') as outputfile:
            duplicatereader = csv.DictReader(inputfile, delimiter=',')
            uniquewrite = csv.DictWriter(outputfile, fieldnames=['company', 'website'], delimiter=',')
            uniquewrite.writeheader()
            keysread = []
            for row in duplicatereader:
               key = (row['company'])
               if key not in keysread:
                   print(row)
                   keysread.append(key)
                   uniquewrite.writerow(row)
#
# """Execute this when run the script first time only"""
# if __name__ == '__main__':
#     main()



csv_data = pd.read_csv('classified_urls_merged.csv', index_col=False, header=0)

general_websites_list = ['facebook', 'linkedin', '1207', '1307', 'kompass', 'companyweb', 'youtube', 'yelp', 'companytracker','data.be', 'infobel', 'bsearch', 'trendstop', 'hoovers','bloomberg','pagesdoor','tuugo','myshopi','yelp','bizbook','bizique','europages','goldenpages','airbnb','194.7.35.240','info-clipper','goudengids','handelsgids','pdv.apixml.net','belgiancompanies','food','cadastre','transport-international','infos-bruxelles','lacapitale','belgian.company','tripadvisor','kadaster','fr.autoscout24.be','bedrijvenpagina','twitter','belgium-services','booking','info-brabant-wallon','staatsbladmonitor','users.skynet.bet','heures','avelgem','cylex','numero-pro','autoscout24','openingsuren','foursquare','truckscout24','maasmechelen','church.cybo','companycheck']

general_websites = []
company_websites = []
website = []


def classify_emails():
    for row in csv_data.itertuples():
        # print(row[2:4])

        get_website = row.website
        get_website_lower = str(get_website).lower()

        for i in general_websites_list:
            try:
                if len(row) == 0:
                    continue
                else:
                    if -1 != get_website_lower.find(i):
                        general_websites.append(get_website_lower)

            except ValueError:
                print('No result')
                continue

        if get_website_lower not in general_websites:
            website.append(*row[1:2]) # unpacking tuples
            company_websites.append(get_website_lower)

    classified_csv()


def classified_csv():

    # df1 = pd.DataFrame(general_websites, columns=['General'])
    df2 = pd.DataFrame(company_websites, website)
    # df1.reset_index(drop=False)
    # df2.reset_index(drop=False)
    # df = pd.concat([df1, df2], axis=1)
    # df.dropna()
    df2.drop_duplicates(inplace=True)
    # df2.index = df2.index + 1
    df2.to_csv('classified.csv')
    return df2


classify_emails()
