import pandas as pd


def export_mappings(dir_out):
    """Export mappings to csv files
    :param dir_out: <string> output path
    """
    maps = {
        "accountTypeCodes.csv": map_account_type,
        "unitTypeCodes.csv": map_unitType,
        "registryCodes.csv": map_registryCodes,
        "activityCodes.csv": map_activity,
        "complianceCodes.csv": map_complianceCode,
        "mainTransactionTypeCodes.csv": map_trans_type,
        "supplementaryTransactionTypeCodes.csv": map_trans_supp_type,
        "tradingSystemCodes.csv": map_tradingSystem,
    }
    for fn, data in maps.items():
        pd.DataFrame(data.items(), columns=["code", "description"]).to_csv(
            dir_out + fn, index=False
        )


map_unitType_inv = {
    "CER - Certified Emission Reduction Unit": "CER",
    "EU General Allowances (EUA)": "EUA_2013",
    "EU Aviation Allowances (EUAA)": "AEUA",
    "ERU - Emission Reduction Unit (Converted from an AAU)": "ERU",
    "AAU - Assigned Amount Unit - Allowance issued for the 2008-2012 period and subsequent 5-year periods and is converted from an AAU": "EUA_2008",
    "Allowance issued for the 2005-2007 period and not converted from an AAU or other Kyoto unit": "EUA2005",
    "Swiss Aviation Allowances (CHUA)": "CHUA",
    "Swiss General Allowances (CHU)": "CHU",
    "RMU - Removal Unit": "RMU",
    "ERU - Emission Reduction Unit (Converted from an RMU)": "ERU_RMU",
    "tCER - Temporary CER": "tCER",
    "AAU - Assigned Amount Unit": "AAU",
    "AEA - Annual Emissions Allocations": "AEA",
    "International Credit": "credit",
}

map_unitType = {v: k for k, v in map_unitType_inv.items()}

map_account_type = {
    "100-7": "Operator Holding Account",
    "120-0": "Former Operator Holding Account",
    "100-9": "Aircraft Operator Account",
    "100-8": "Person Holding Account",
    "121-0": "Person Account in National Registry",
    "100-12": "Trading Account",
    "100-13": "Auction Delivery Account",
    "0-10": "Verifier Account",
    "0-11": "External Platform Holding Account",
    "110-0": "Pending Account",
    "100-0": "Party Holding Account",
    "100-2": "National Allowance Holding Account",
    "100-5": "Union Allowance Deletion Account",
    "100-14": "Auction Account",
    "100-15": "Aviation Auction Account",
    "100-16": "Total Quantity Account",
    "100-17": "Aviation Total Quantity Account",
    "100-18": "New Entrant Reserve Account",
    "100-19": "Special Reserve Account",
    "100-20": "Allocation Account",
    "100-21": "Aviation Allocation Account",
    "100-1": "AAU Deposit Account",
    "100-3": "Central Clearing Account",
    "100-4": "Gateway Deposit Account",
    "100-24": "AEA Total quantity Account",
    "280-0": "Ambition Increase Cancellation Account (Type 8)",
    "270-0": "Article 3.7ter Cancellation Account (Type 7)",
    "241-0": "CCS Net Reversal Cancellation Account",
    "130-0": "Previous Period Surplus Reserve Account (PPSR)",
    "100-6": "Aviation Surrender Set-Aside Account",
    "100-25": "ESD Compliance Account",
    "210-0": "Net Source Cancellation Account (Type 1)",
    "100-26": "AEA Deletion Account",
    "220-0": "Non-compliance Cancellation Account (Type 2)",
    "230-0": "Voluntary Cancellation Account (Type 3)",
    "240-0": "Excess Issuance Cancellation Account (Type 4)",
    "250-0": "Mandatory (Cancellation Account (Type 5)",
    "300-0": "Retirement Account",
    "411-0": "tCER Replacement Account for Expiry (Type 1)",
    "421-0": "lCER Replacement Account for Expiry (Type 1)",
    "422-0": "lCER Replacement Account for Reversal in Storage (Type 2)",
    "423-0": "lCER Replacement Account for Non-submission of Certification Report (Type 3)",
    "100-27": "EU AAU Account",
    "100-31": "ETS Central Clearing Account for CP2",
    "100-29": "ESD Central Clearing Account",
    "100-28": "ETS AAU Deposit Account",
    "100-30": "ESD AAU Deposit Account",
    "242-0": "Non Submission Of Verification Report Cancellation Account",
    "100-22": "International Credit Account",
    "100-23": "Credit Exchange Account",
    # ESD accounts
    "esd": "EU Effort Sharing Account",
}

map_account_type_inv = {v: k for k, v in map_account_type.items()}

map_registryCodes = {
    "AT": "Austria",
    "BE": "Belgium",
    "BG": "Bulgaria",
    "HR": "Croatia",
    "CY": "Cyprus",
    "CZ": "Czech Republic",
    "DK": "Denmark",
    "ED": "ESD",
    "EE": "Estonia",
    "EU": "European Commission",
    "FI": "Finland",
    "FR": "France",
    "DE": "Germany",
    "GR": "Greece",
    "HU": "Hungary",
    "IS": "Iceland",
    "IE": "Ireland",
    "IT": "Italy",
    "LV": "Latvia",
    "LI": "Liechtenstein",
    "LT": "Lithuania",
    "LU": "Luxembourg",
    "MT": "Malta",
    "NL": "Netherlands",
    "NO": "Norway",
    "PL": "Poland",
    "PT": "Portugal",
    "RO": "Romania",
    "SK": "Slovakia",
    "SI": "Slovenia",
    "ES": "Spain",
    "SE": "Sweden",
    "GB": "United Kingdom",
    "AF": "Afghanistan",
    "AX": "Aland Islands",
    "AL": "Albania",
    "DZ": "Algeria",
    "AS": "American Samoa",
    "AD": "Andorra",
    "AO": "Angola",
    "AI": "Anguilla",
    "AQ": "Antarctica",
    "AG": "Antigua And Barbuda",
    "AR": "Argentina",
    "AM": "Armenia",
    "AW": "Aruba",
    "AU": "Australia",
    "AZ": "Azerbaijan",
    "BS": "Bahamas",
    "BH": "Bahrain",
    "BD": "Bangladesh",
    "BB": "Barbados",
    "BY": "Belarus",
    "BZ": "Belize",
    "BJ": "Benin",
    "BM": "Bermuda",
    "BT": "Bhutan",
    "BO": "Bolivia",
    "BQ": "Bonaire, Sint Eustatius and Saba",
    "BA": "Bosnia And Herzegovina",
    "BW": "Botswana",
    "BV": "Bouvet Island",
    "BR": "Brazil",
    "IO": "British Indian Ocean Territory",
    "BN": "Brunei Darussalam",
    "BF": "Burkina Faso",
    "BI": "Burundi",
    "CDM": "CDM",
    "KH": "Cambodia",
    "CM": "Cameroon",
    "CA": "Canada",
    "CV": "Cape Verde",
    "KY": "Cayman Islands",
    "CF": "Central African Republic",
    "TD": "Chad",
    "CL": "Chile",
    "CN": "China",
    "CX": "Christmas Island",
    "CC": "Cocos (Keeling) Islands",
    "CO": "Colombia",
    "KM": "Comoros",
    "CG": "Congo",
    "CD": "Congo, The Democratic Republic Of The",
    "CK": "Cook Islands",
    "CR": "Costa Rica",
    "CI": "Cote D&#39;Ivoire",
    "CU": "Cuba",
    "CW": "Curacao",
    "CY0": "Cyprus CP0",
    "DJ": "Djibouti",
    "DM": "Dominica",
    "DO": "Dominican Republic",
    "EC": "Ecuador",
    "EG": "Egypt",
    "SV": "El Salvador",
    "GQ": "Equatorial Guinea",
    "ER": "Eritrea",
    "ET": "Ethiopia",
    "FK": "Falkland Islands (Malvinas)",
    "FO": "Faroe Islands",
    "FJ": "Fiji",
    "GF": "French Guiana",
    "PF": "French Polynesia",
    "TF": "French Southern Territories",
    "GA": "Gabon",
    "GM": "Gambia",
    "GE": "Georgia",
    "GH": "Ghana",
    "GI": "Gibraltar",
    "GL": "Greenland",
    "GD": "Grenada",
    "GP": "Guadeloupe",
    "GU": "Guam",
    "GT": "Guatemala",
    "GN": "Guinea",
    "GW": "Guinea-Bissau",
    "GY": "Guyana",
    "HT": "Haiti",
    "HM": "Heard Island And Mcdonald Islands",
    "VA": "Holy See (Vatican City State)",
    "HN": "Honduras",
    "HK": "Hong Kong",
    "ITL": "ITL",
    "IN": "India",
    "ID": "Indonesia",
    "IR": "Iran, Islamic Republic Of",
    "IQ": "Iraq",
    "IL": "Israel",
    "JM": "Jamaica",
    "JP": "Japan",
    "JE": "Jersey",
    "JO": "Jordan",
    "KZ": "Kazakhstan",
    "KE": "Kenya",
    "KI": "Kiribati",
    "KP": "Korea, Democratic People&#39;S Republic Of",
    "KR": "Korea, Republic Of",
    "KW": "Kuwait",
    "KG": "Kyrgyzstan",
    "LA": "Lao People&#39;S Democratic Republic",
    "LB": "Lebanon",
    "LS": "Lesotho",
    "LR": "Liberia",
    "LY": "Libyan Arab Jamahiriya",
    "MO": "Macao",
    "MK": "Macedonia, The Former Yugoslav Republic Of",
    "MG": "Madagascar",
    "MW": "Malawi",
    "MY": "Malaysia",
    "MV": "Maldives",
    "ML": "Mali",
    "MT0": "Malta CP0",
    "MH": "Marshall Islands",
    "MQ": "Martinique",
    "MR": "Mauritania",
    "MU": "Mauritius",
    "YT": "Mayotte",
    "MX": "Mexico",
    "FM": "Micronesia, Federated States Of",
    "MD": "Moldova, Republic Of",
    "MC": "Monaco",
    "MN": "Mongolia",
    "MS": "Montserrat",
    "MA": "Morocco",
    "MZ": "Mozambique",
    "MM": "Myanmar",
    "NA": "Namibia",
    "NR": "Nauru",
    "NP": "Nepal",
    "NC": "New Caledonia",
    "NZ": "New Zealand",
    "NI": "Nicaragua",
    "NE": "Niger",
    "NG": "Nigeria",
    "NU": "Niue",
    "NF": "Norfolk Island",
    "MP": "Northern Mariana Islands",
    "OM": "Oman",
    "PK": "Pakistan",
    "PW": "Palau",
    "PS": "Palestinian Territory, Occupied",
    "PA": "Panama",
    "PG": "Papua New Guinea",
    "PY": "Paraguay",
    "PE": "Peru",
    "PH": "Philippines",
    "PN": "Pitcairn",
    "PR": "Puerto Rico",
    "QA": "Qatar",
    "RE": "Reunion",
    "RU": "Russian Federation",
    "RW": "Rwanda",
    "BL": "Saint Barthelemy",
    "SH": "Saint Helena",
    "KN": "Saint Kitts And Nevis",
    "LC": "Saint Lucia",
    "MF": "Saint Martin (French part)",
    "PM": "Saint Pierre And Miquelon",
    "VC": "Saint Vincent And The Grenadines",
    "WS": "Samoa",
    "SM": "San Marino",
    "ST": "Sao Tome And Principe",
    "SA": "Saudi Arabia",
    "SN": "Senegal",
    "CS": "Serbia And Montenegro",
    "SC": "Seychelles",
    "SL": "Sierra Leone",
    "SG": "Singapore",
    "SX": "Sint Maarten (Dutch part)",
    "SB": "Solomon Islands",
    "SO": "Somalia",
    "ZA": "South Africa",
    "GS": "South Georgia And The South Sandwich Islands",
    "SS": "South Sudan",
    "LK": "Sri Lanka",
    "SD": "Sudan",
    "SR": "Suriname",
    "SJ": "Svalbard And Jan Mayen",
    "SZ": "Swaziland",
    "CH": "Switzerland",
    "SY": "Syrian Arab Republic",
    "TW": "Taiwan, Province Of China",
    "TJ": "Tajikistan",
    "TZ": "Tanzania, United Republic Of",
    "TH": "Thailand",
    "TL": "Timor-Leste",
    "TG": "Togo",
    "TK": "Tokelau",
    "TO": "Tonga",
    "TT": "Trinidad And Tobago",
    "TN": "Tunisia",
    "TR": "Turkey",
    "TM": "Turkmenistan",
    "TC": "Turks And Caicos Islands",
    "TV": "Tuvalu",
    "UG": "Uganda",
    "UA": "Ukraine",
    "AE": "United Arab Emirates",
    "US": "United States",
    "UM": "United States Minor Outlying Islands",
    "UY": "Uruguay",
    "UZ": "Uzbekistan",
    "VU": "Vanuatu",
    "VE": "Venezuela",
    "VN": "Viet Nam",
    "VG": "Virgin Islands, British",
    "VI": "Virgin Islands, U.S.",
    "WF": "Wallis And Futuna",
    "EH": "Western Sahara",
    "YE": "Yemen",
    "ZM": "Zambia",
    "ZW": "Zimbabwe",
    "XI": "Northern Ireland",
    "ESD": "Effort Sharing Management",
}

map_registryCode_inv = {v: k for k, v in map_registryCodes.items()}


map_activity = {
    20: "Combustion of fuels",
    21: "Refining of mineral oil",
    22: "Production of coke",
    23: "Metal ore roasting or sintering",
    24: "Production of pig iron or steel",
    25: "Production or processing of ferrous metals",
    26: "Production of primary aluminium",
    27: "Production of secondary aluminium",
    28: "Production or processing of non-ferrous metals",
    29: "Production of cement clinker",
    30: "Production of lime, or calcination of dolomite/magnesite",
    31: "Manufacture of glass",
    32: "Manufacture of ceramics",
    33: "Manufacture of mineral wool",
    34: "Production or processing of gypsum or plasterboard",
    35: "Production of pulp",
    36: "Production of paper or cardboard",
    37: "Production of carbon black",
    38: "Production of nitric acid",
    39: "Production of adipic acid",
    40: "Production of glyoxal and glyoxylic acid",
    41: "Production of ammonia",
    42: "Production of bulk chemicals",
    43: "Production of hydrogen and synthesis gas",
    44: "Production of soda ash and sodium bicarbonate",
    45: "Capture of greenhouse gases under Directive 2009/31/EC",
    46: "Transport of greenhouse gases under Directive 2009/31/EC",
    47: "Storage of greenhouse gases under Directive 2009/31/EC",
    1: "Combustion installations with a rated thermal input exceeding 20 MW",
    2: "Mineral oil refineries",
    3: "Coke ovens",
    4: "Metal ore (including sulphide ore) roasting or sintering installations",
    5: "Installations for the production of pig iron or steel (primary or secondary fusion) including continuous casting",
    6: "Installations for the production of cement clinker in rotary kilns or lime in rotary kilns or in other furnaces",
    7: "Installations for the manufacture of glass including glass fibre",
    8: "Installations for the manufacture of ceramic products by firing, in particular roofing tiles, bricks, refractory bricks, tiles, stoneware or porcelain",
    9: "Industrial plants for the production of (a) pulp from timber or other fibrous materials (b) paper and board",
    10: "Aircraft operator activities",
    99: "Other activity opted-in pursuant to Article 24 of Directive 2003/87/EC",
    # esd activities
    1000: "EU Effort Sharing",
}

map_activity_data_to_code = {"%d-%s" % (k, v): k for k, v in map_activity.items()}

map_activity_data_to_name = {"%d-%s" % (k, v): v for k, v in map_activity.items()}


map_complianceCode = {
    "A": "The number of allowances and ERUs/CERs surrendered by 30 April is greater than or equal to verified emissions",
    "B": "The number of allowances and ERUs/CERs surrendered by 30 April is lower than verified emissions",
    "C": "Verified emissions were not entered until 30 April",
    "D": "Verified emissions were corrected by competent authority after 30 April of year X. The competent authority of the Member State decided that the installation is not in compliance for year X-1",
    "E": "Verified emissions were corrected by competent authority after 30 April of year X. The competent authority of the Member State decided that the installation is in compliance for year X-1",
    "X": "Entering verified emissions and/or surrendering was impossible until 30 April due to the allowance surrender process and/or verified emissions update process being suspended for the Member State's registry",
    "-": "No Compliance Obligations",
    "Compliant": "Compliant under ESD",
}


map_trans_type = {
    1: "Issuance - Initial creation of a unit",
    10: "Internal - Internal transfer of unit/supplementary program transaction",
    2: "Conversion - Transformation of unit to create an ERU",
    3: "External - External transfer of unit between registries",
    4: "Cancellation - Internal transfer of unit",
    5: "Retirement - Internal transfer of unit",
    6: "Replacement - Internal transfer of unit",
    7: "Carry-over - Change of validity to subsequent CP",
    8: "Expiry Date Change",
}


map_trans_supp_type = {
    0: "No Supplementary Type",
    1: "Allowance cancellation (2005-2007)",
    104: "Reversal of cancellation",
    11: "ESD AEA Allocation",
    113: "ESD Reversal AEA Carry Forward",
    114: "ESD Reversal AEA Carry Over",
    115: "ESD Reversal AEA Transfer",
    12: "ESD KP Transfer from PHA",
    124: "Reversal of cancellation",
    13: "ESD AEA Carry Forward",
    135: "Allocation of aviation allowances",
    136: "Allocation of general allowances",
    14: "ESD AEA Carry Over",
    142: "Reversal Transfer Entitlement",
    143: "Reversal Carry Over Entitlement",
    15: "ESD AEA Transfer",
    16: "ESD Return to KP after Compliance",
    17: "ESD Delete AEA after Compliance",
    171: "Reversal of Exchange",
    172: "Reversal of Transfer of Exchanged",
    18: "ESD Delete After Overallocation",
    19: "Retirement ESD Used Units",
    190: "Reversal of deletion",
    2: "Allowance surrender",
    21: "External transfer (2005-2007)",
    22: "External transfer between art63a registries",
    24: "Issuance - Internal transfer Art 63a",
    26: "Conversion of art63a allowances",
    272: "Reversal of Issuance of Exchanged",
    3: "Retirement (2005-2007)",
    30: "Issuance of aviation allowances",
    31: "Issuance of general allowances",
    33: "Aviation allowances - Banking",
    34: "General allowances - Banking",
    35: "Allocation of aviation allowances",
    36: "Allocation of general allowances",
    37: "Auction delivery",
    38: "Carry Over of CERs or ERUs converted from AAUs",
    39: "Carry Over of AAUs",
    4: "Surrender Kyoto Units from AOHA",
    41: "Cancellation and replacement",
    42: "Transfer Entitlement",
    43: "Carry Over Entitlement",
    44: "ESD Reversal KP Transfer",
    45: "Article 3.7ter Cancellation",
    46: "Ambition Increase Cancellation",
    47: "Transfer to SOP for First External Transfer of AAUs",
    48: "Mandatory Cancellation",
    49: "Transfer to SOP for Conversion",
    51: "Allowance issue (2005-2007)",
    52: "Allowance issue (2008-2012 onwards)",
    53: "Allowance allocation",
    54: "Force-majeure allowance issue",
    55: "Correction to allowances",
    56: "Conversion prior to Transfer to SOP (Conversion A)",
    57: "Conversion of AAUs or RMUs into ERUs (Conversion B)",
    61: "Surrendered Allowance Conversion",
    62: "Unallocated Allowance Conversion",
    71: "Exchange",
    72: "Exchanged",
    75: "75-AAU set aside",
    82: "Reversal of surrender",
    84: "Reversal of Surrender Kyoto Units from AOHA",
    86: "Reverse of Excess Allocation",
    90: "Deletion of allowances",
    91: "Cancellation against deletion",
    92: "Reversal of Allowance Surrender",
    93: "Correction",
    94: "Reversal of Allowance Cancellation",
}

map_tradingSystem = {
    "euets": "EU Emissions Trading System",
    "esd": "EU Effort Sharing Decision",
    "chets": "Swiss Emissions Trading System",
}
