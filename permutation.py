import argparse

parser = argparse.ArgumentParser(description='Please input the company name')
parser.add_argument('--company', help='give the company name for permutation')
args = parser.parse_args()
company_name = args.company

def read_subdomain_list():
    lines = []
    with open("subdomains-top1mil-110000.txt", "r") as text_file:
        lines = map(lambda x: x.replace('\n', ''), text_file.readlines())
    return lines

def generate_permutation(company_name):
    with open("permutation-{}.txt".format(company_name), "w") as permutation_file:
        for element in read_subdomain_list():
            permutation_str = company_name + '-' + element
            permutation_file.write(permutation_str + '\n')


if __name__ == "__main__":
    # execute only if run as a script
    generate_permutation(company_name)
