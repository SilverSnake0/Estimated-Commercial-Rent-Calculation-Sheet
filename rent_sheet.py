# James L. is the developer and also a commercial real estate associate broker.
# This real estate rent table program is provided as is. There are no warranties about the completeness, reliability and accuracy of this information. Any action you take upon the information in this program, is strictly at your own risk. The developer will not be held responsible for any damages, losses, or other negative consequences resulting from the use of this program. The user assumes all risks and liabilities associated with using this program. Thank you!  @Copyright 2022

# Try to import pandas to generate the excel table if the user wants to save the table as an .xlsx file
try:
    import pandas as pd
except:
    pass

def exit_main():
    exit()

def main():
    rent_sheet = []
    print('██     ██ ███████ ██       ██████  ██████  ███    ███ ███████  ')                                  
    print('██     ██ ██      ██      ██      ██    ██ ████  ████ ██       ')                                        
    print('██  █  ██ █████   ██      ██      ██    ██ ██ ████ ██ █████                                       Created by: James L.')                                    
    print('██ ███ ██ ██      ██      ██      ██    ██ ██  ██  ██ ██                                              @Copyright 2023')                                   
    print(' ███ ███  ███████ ███████  ██████  ██████  ██      ██ ███████ ')  
    print(' _          _   _          _____     _   _           _         _    _____                             _     _    _____         _      _____ _           _  ')
    print('| |_ ___   | |_| |_ ___   |   __|___| |_|_|_____ ___| |_ ___ _| |  |     |___ _____ _____ ___ ___ ___|_|___| |  | __  |___ ___| |_   |   __| |_ ___ ___| |_')
    print("|  _| . |  |  _|   | -_|  |   __|_ -|  _| |     | .'|  _| -_| . |  |   --| . |     |     | -_|  _|  _| | .'| |  |    -| -_|   |  _|  |__   |   | -_| -_|  _|")
    print('|_| |___|  |_| |_|_|___|  |_____|___|_| |_|_|_|_|__,|_| |___|___|  |_____|___|_|_|_|_|_|_|___|_| |___|_|__,|_|  |__|__|___|_|_|_|    |_____|_|_|___|___|_|  ')
    
    # Column name headers list
    columns = ['Lease Year', 'Rent Per SF', 'Square Footage', 'Annual Escalation', 'Monthly Rent', 'Annual Rent', 'NNN Per SF', 'Monthly NNN', 'Gross Annual Rent', 'Percentage Rent', 'Percentage Breakpoint']
    # Function to show user did not input an integer number, this will display a integer error and restart the program.
    def integer_error():
        print('▓█████  ██▀███   ██▀███   ▒█████   ██▀███  ')
        print('▓█   ▀ ▓██ ▒ ██▒▓██ ▒ ██▒▒██▒  ██▒▓██ ▒ ██▒')
        print('▒███   ▓██ ░▄█ ▒▓██ ░▄█ ▒▒██░  ██▒▓██ ░▄█ ▒')
        print('▒▓█  ▄ ▒██▀▀█▄  ▒██▀▀█▄  ▒██   ██░▒██▀▀█▄  ')
        print('░▒████▒░██▓ ▒██▒░██▓ ▒██▒░ ████▓▒░░██▓ ▒██▒')
        print('░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░')
        print(' ░ ░  ░  ░▒ ░ ▒░  ░▒ ░ ▒░  ░ ▒ ▒░   ░▒ ░ ▒░')
        print('  ░     ░░   ░   ░░   ░ ░ ░ ░ ▒    ░░   ░ ')
        print('  ░  ░   ░        ░         ░ ░     ░     ')
        print('                                          ')
        print('\n You Must Enter a Valid Integer Number.\n')
        print('\n Valid Integer Number Examples: 5, 50, 5000\n')
        print('\n Invalid Non-Integer Number Examples: @, .05, (5)\n')
        try:
            input('Press enter to restart...\n')
        except:
            exit_main()
        main()
    # Function to show user did not input a float number, this will display a float error and restart the program.
    def float_error():
        print('▓█████  ██▀███   ██▀███   ▒█████   ██▀███  ')
        print('▓█   ▀ ▓██ ▒ ██▒▓██ ▒ ██▒▒██▒  ██▒▓██ ▒ ██▒')
        print('▒███   ▓██ ░▄█ ▒▓██ ░▄█ ▒▒██░  ██▒▓██ ░▄█ ▒')
        print('▒▓█  ▄ ▒██▀▀█▄  ▒██▀▀█▄  ▒██   ██░▒██▀▀█▄  ')
        print('░▒████▒░██▓ ▒██▒░██▓ ▒██▒░ ████▓▒░░██▓ ▒██▒')
        print('░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░')
        print(' ░ ░  ░  ░▒ ░ ▒░  ░▒ ░ ▒░  ░ ▒ ▒░   ░▒ ░ ▒░')
        print('  ░     ░░   ░   ░░   ░ ░ ░ ░ ▒    ░░   ░ ')
        print('  ░  ░   ░        ░         ░ ░     ░     ')
        print('                                          ')
        print('\n You Must Enter a Valid Float Number.\n')
        print('\n Valid Float Number Examples: .05, .5, .50\n')
        print('\n Invalid Non-Float Number Examples: @, 5%, (5)\n')
        try:
            input('Press enter to restart...\n')
        except:
            exit_main()
        main()
    # Goodbye message at the exit of the program. 
    def take_care():
        print('_/_/_/_/_/          _/                        _/_/_/                                _/   ')
        print('   _/      _/_/_/  _/  _/      _/_/        _/          _/_/_/  _/  _/_/    _/_/    _/    ')
        print('  _/    _/    _/  _/_/      _/_/_/_/      _/        _/    _/  _/_/      _/_/_/_/  _/     ')
        print(' _/    _/    _/  _/  _/    _/            _/        _/    _/  _/        _/                ')
        print('_/      _/_/_/  _/    _/    _/_/_/        _/_/_/    _/_/_/  _/          _/_/_/  _/       ')

    # Adding the lease term column function.
    def add_term(years):
        for i in range(years):
            rent_sheet.append([i+1])

    # Taking user input for the lease term.
    try:
        years = int(input('[Lease Year]\nPlease enter how many years in the initial lease term:'))
    except:
        integer_error()
    add_term(years)        
    # Adding the rent per square foot to the column function.
    def add_rent_psf(rent_psf):
        for i in rent_sheet:
            i.append(rent_psf)
    # Taking user input for the rent per square foot.
    try:
        rent_psf = float(input('[Rent Per SF]\nPlease enter the rent amount per square foot:'))
    except:
        float_error()
    add_rent_psf(rent_psf)    
    # Adding the square foot to the column function.
    def add_sf(sf):
        for i in rent_sheet:
            i.append(sf)
    # Taking user input for the square footage number.
    try:
        sf = int(input('[SF]\nPlease enter the square footage of the space:'))
    except:
        integer_error()
    add_sf(sf)
    # Taking user input for the annual escalation. 
    try:
        num = float(input('[Annual Esc]\nPlease enter the starting annual escalation percentage (e.g., ".03" for 3%):'))
    except:
        float_error()
     # Custom annual escalation function if user wanted to lock the rent sequentially for a certain number of years, usually fortune 500 fast food chains would have rent locks about every five years before a rent increase.
    def custom_escalation(num, step):
        count = step 
        for i in rent_sheet:
            if count > 0:
                i.append(0)
                count -= 1
            else:
                i.append(num)
                count = step - 1
    # Adding the normal escalation function for rent to increase every year.
    def add_annual_escalation(num, rentlock):
            if rentlock == 0:
                for i in rent_sheet:
                    i.append(num)
            else:
                for i in rent_sheet[0:rentlock]:
                    i.append(0)
                for i in rent_sheet[rentlock:]:
                    i.append(num)      
    # Taking the user integer input for a rent lock of the first few years, 999 for the custom escalation function, entering 0 will initiate the normal escalation function.    
    try:
        rentlock = int(input('[Rent Lock]\nIf applicable, please enter the number of starting years the rent will be locked for (Enter "0" if this doesn\'t apply, or enter "999" to customize the rent lock):'))
    except:
        integer_error()

    if rentlock == 999:
        try:
            step = int(input('[Rent Lock SEQ]\nPlease enter the amount of years the rent shall be locked sequentially:'))
            custom_escalation(num, step)
        except:
            integer_error()
    else:
        add_annual_escalation(num, rentlock)
    # Adjusting the rent per sf to account for the rent escalation.
    def rent_esc():
        rent_sheet[0][3] = 0
        current_rent_psf = rent_sheet[0][1]
        for i in rent_sheet[1:]:
            current_esc = 1 + i[3]
            current_rent_psf *= current_esc
            i[1] = round(current_rent_psf, 2)
    
    rent_esc()
    # Generating the annual rent and monthly rent inside the rent sheet.
    def calc_rent():
        annual_rent = rent_sheet[0][1] * rent_sheet[0][2]
        annual_escalation = 0
        count = 1
        for i in rent_sheet:
            if count == 1:
                starting_annual_rent = i[1] * i[2]
                annual_escalation = 1 + i[3]
                i.append(round(annual_rent / 12, 2))
                i.append(round(annual_rent, 2))
                count -= 1
                annual_rent = starting_annual_rent
            else:
                annual_escalation = 1 + i[3]
                annual_rent *= annual_escalation
                i.append(round(annual_rent / 12,2))
                i.append(round(annual_rent,2))

    calc_rent()
    # Adding the triple net per square foot column function for the expense total of common area maintenance, insurance, and real estate taxes.    
    def add_triple_net(nnn):
        if nnn == 999:
            try:
                nnn_esc = float(input('[NNN Esc]\nPlease enter the fixed annual escalation percentage for the triple nets (e.g., ".03" for 3%):'))
            except:
                float_error()
            try:
                new_nnn = float(input('[NNN per SF]\nPlease enter the triple net per square foot amount:'))
            except:
                float_error()
            current_nnn = new_nnn * (1 + nnn_esc)
            count = 0
            for i in rent_sheet:
                if count != 0:
                    i.append(round(new_nnn, 2))
                    count -= 1
                else:
                    i.append(round(current_nnn, 2))
                    current_nnn = current_nnn * (1 + nnn_esc)
        else:
            for i in rent_sheet:
                i.append(nnn) 
    # Taking user input for the triple net amount.
    try:
        nnn = float(input('[NNN per SF]\nPlease enter the triple net per square foot amount (or enter "999" for triple nets with fixed annual escalation):'))
    except:
        float_error()
    add_triple_net(nnn)
    # Using the total triple net amount and calculating the monthly triple net expense based on the square footage, and adding to column.
    def calc_monthly_triple_net():
        for i in rent_sheet:
            net = i[6] * i[2] / 12
            i.append(round(net, 2)) 

    calc_monthly_triple_net()
    # Function to calculate the total rent paid after twelve months and adding to column.
    def calc_gross_annual_rent():
        for i in rent_sheet:
            gross_annual_rent = i[5] + (i[7] * 12)
            i.append(round(gross_annual_rent, 2))

    calc_gross_annual_rent()
    # Function to add the percentage rent that landlord takes should the tenant exceed a certain gross sales threshold.
    def percentage_rent(percentage):
        for i in rent_sheet:
            i.append(percentage)
    # Taking user input for the percentage rent amount
    try:
        percentage = float(input('[% Rent]\nPlease enter the percentage rent amount (e.g., ".06" for 6%), or type "0" for none:'))
        percentage_rent(percentage)
    except:
        float_error()
    # Function to calculate the un-natural breakpoint should the tenant negotiate not to go with a natural breakpoint. Unnatural breakpoints here would be escalated based on the current annual escalation number for the lease year.
    def calc_unnatural_breakpoint(unnatural):
        current_breakpoint = unnatural
        count = 1
        for i in rent_sheet:
            if count != 0:
                i.append(current_breakpoint)
                count -= 1
            else:
                current_breakpoint *= (1 + i[3])
                rounded_breakpoint = round(current_breakpoint, 2)
                i.append(rounded_breakpoint)
    # Taking the user input for the un-natural breakpoint and adding code that if the percentage rent is 0, the following code will not run.
    unnat = 0
    if percentage != 0:
        try:
            unnatural = int(input('[U-NAT % Rent]\nIf applicable, please enter the un-natural percentage breakpoint amount (INTEGER #), or type "0" for none:'))
            unnat = unnatural
        except:
            integer_error()
    # Function to calculate the natural percentage breakpoint and removing the percentage rent columns if percentage rent does not exist.
    def calc_percentage_breakpoint():
        if (unnat == 0) & (percentage == 0):
            for i in rent_sheet:
                del i[-1]
            del columns[-2:]
        else:
            for i in rent_sheet:
                percentage_breakpoint = round(i[5] / i[9], 2)
                i.append(percentage_breakpoint)
    # Finding out if the user is going with natural percentage breakpoint or unnatural percentage breakpoint, and running the proper function.
    if unnat != 0 or '':
        calc_unnatural_breakpoint(unnat)
    else:
        calc_percentage_breakpoint()

    # Adding a function for the user to show a specific year. The function would take items from both the column headers and rent sheet, and would combine them together for easier readability.
    def show(year):
        new_sheet = [item for title in zip(columns, rent_sheet[year - 1]) for item in title]
        try:
            print(f'{"⧓" * 100}\n{new_sheet}\n{"⧓" * 100}')
        finally:
            pass
    # Taking the user input for the year they want to view, and calling the show function with the year as the first argument.
        try:
            show_year = int(input('\nWould you like to select another year? If yes, please enter a lease year, or enter "0" to return to the main menu:\n'))
        except:
            integer_error()
        if show_year == 0:
            main_menu()
        elif (show_year > 0) and (show_year < rent_sheet[-1][0]):
            print(f'\nShowing Lease Year: {show_year}')
            show(show_year)
        else:
            print('\nThe number you entered does not exist in the lease term.\n')
    # Function to calculate the broker commission fee up to the first 10 years of the initial term.
    write_broker_commission = 0
    write_company_commission = 0
    def calc_commission(fee):
        nonlocal write_broker_commission, write_company_commission
        try:
            company_split = float(input('\nWhat is the broker commission split with the company (e.g., ".5" for 50%):\n'))
            total = 0
            count = 10
        except:
            float_error()
        for i in rent_sheet:
            if count > 0:
                total += i[5]
                count -= 1
        broker_commission = round(total * fee * company_split, 2)
        write_broker_commission += broker_commission
        company_commission = round((total * fee) - broker_commission, 2)
        write_company_commission += company_commission
        print(f'\nThe broker fee based on the total rent paid by the tenant for 10 years is estimated to be : ${round(total * fee, 2)}')
        print(f'\nCompany split is: ${company_commission}                  {100 - (company_split * 100)}% / {company_split * 100}%                  Broker split is: ${broker_commission}')
        input('\nPress enter to continue...')
        try:
            main_menu()
        except:
            pass
    # Function to calculate the base rent and gross rent (including triple net) paid over the entire lease term.
    def calc_total_rent_paid():
        base_rent_total = 0
        gross_rent_total = 0
        for i in rent_sheet:
            base_rent_total += i[5]
            gross_rent_total += i[8]

        print(f'{"◚" * 100}')
        print(f'\nThe total base rent paid by the tenant is estimated to be ${round(base_rent_total, 2)}\n')
        print(f'The total gross rent paid by the tenant is estimated to be ${round(gross_rent_total, 2)}\n')
        print(f'{"◛" * 100}')
        input('Press enter to continue...')
        try:
            main_menu()
        except:
            pass
    # Added function to calculate landlord concessions to Tenant and Tenant's security and guaranty for the space.
    write_ti = 0
    write_free_rent = 0
    write_guaranty = 0
    write_deposit = 0
    def calc_landlord_concessions():
        nonlocal write_ti, write_free_rent, write_guaranty, write_deposit
        try:
            ti = int(input('[TI per SF]\nPlease enter the amount of tenant improvement allowance per square foot that landlord has provided to the tenant:'))
            write_ti += ti
        except:
            integer_error()
        try:
            free_rent = float(input('[FREE RENT]\nPlease enter the number of months of rent abatement the landlord is providing to the tenant:'))
            write_free_rent += free_rent
            guaranty = float(input('[GUARANTY]\nPlease enter the amount of years the tenant is guaranteeing the lease:'))
            write_guaranty += guaranty
            security_deposit = float(input('[SECURITY DEPOSIT]\nPlease enter the amount of months the tenant is providing as a security deposit:'))
            write_deposit += security_deposit
        except:
            float_error()
        # Variables and counters to help the functions below calculate.
        total_free_rent = 0
        guaranty_yr = guaranty * 12
        total_guaranty = 0
        total_deposit = 0
        sec_depo = security_deposit
        free_rent_num = free_rent
        space_sf = rent_sheet[0][2]
        recoup_time = 0
        
        # Calculation for the guaranty provided by the tenant.
        for i in rent_sheet:
            current_annual_rent = i[5]
            if guaranty_yr > 12:
                total_guaranty += (current_annual_rent)
                guaranty_yr -= 12
            else:
                total_guaranty += ((current_annual_rent / 12) * guaranty_yr)
                break
        # Calculation for the total free rent provided by the landlord.    
        for i in rent_sheet:
            current_annual_rent = i[5]
            if free_rent_num > 12:
                total_free_rent += (current_annual_rent)
                free_rent_num -= 12
            else:
                total_free_rent += (current_annual_rent / 12) * free_rent_num
                break
        # Calculation for the total security deposit provided by the tenant.
        for i in rent_sheet:
            gross_monthly_rent = i[4] + ((i[6] * i[2]) / 12)
            if sec_depo > 12:
                total_deposit += gross_monthly_rent * 12
                sec_depo -= 12
            else:
                total_deposit += gross_monthly_rent * sec_depo
                break
        # Calculation for the total of rent abatement and tenant improvement allowance provided by the landlord.
        concessions_count = (ti * space_sf) + total_free_rent
   
        for i in rent_sheet:
            current_annual_rent = i[5]
            if concessions_count > current_annual_rent:
                recoup_time += 1
                concessions_count -= current_annual_rent
            else:
                recoup_time += (concessions_count / current_annual_rent)
                break
        print(f'{"◚" * 100}')
        print(f'\nTotal GUARANTY amount provided from the TENANT: ${round(total_guaranty, 2)}\n')
        print(f'Total SECURITY DEPOSIT amount provided from the TENANT: ${round(total_deposit, 2)}\n')
        print(f'Total RENT ABATEMENT amount provided from the LANDLORD: ${round(total_free_rent, 2)}\n')
        print(f'Total TENANT ALLOWANCE amount provided from the LANDLORD: ${round(ti * space_sf, 2)}\n')
        print(f'Total CONCESSIONS amount provided from the LANDLORD: ${round((ti * space_sf) + total_free_rent, 2)}\n')
        print(f'{"◛" * 100}')
        print(f'\nEstimate time for landlord to recoup concessions from base rent paid: {round(recoup_time, 2)} years ({round(recoup_time * 12, 2)} months)\n')
        input('Press enter to continue...')
        try:
            main_menu()
        except:
            pass
    # Generating the results of all the functions from user input, and adding the column headers to the top of the table.
    class create_table():

        def __init__(self, create_table, display_table):
            self.create_table = create_table          
            self.display_table = display_table        
        def update_column(column):
            index = int(column)
            for i in rent_sheet:
                try:
                    value = float(input(f'Updating column "{columns[index]}" year {i[0]} value to: '))
                except:
                    float_error()
                i[index] = value
            print('\nColumn successfully updated!\n')
            create_table.display_table()
            input('Press enter to continue...')
        # Added a function to have the ability to modify a specific item from a row and column index.
        def update_item(row, column):
            row_index = int(row) - 1
            column_index = int(column)
            try:
                value = float(input(f'Updating Lease Year {row_index + 1} column "{columns[column_index]}" item value to: '))
                rent_sheet[row_index][column_index] = value
            except:
                float_error()
            print('\nItem successfully updated!\n')
            create_table.display_table()
            input('Press enter to continue...')
        #Function that returns the compiled data into a table.
        def display_table():
            nonlocal columns
            print('Creating the rent calculation table...\n')
            print('▄' * 200)
            # Try and except added to check if the percentage rent "columns[9]" and percentage breakpoint "{columns[10]" apply to the rent sheet, if not then those column titles will not be displayed.
            try:
                print(
                    f'{"Lease Year":<7}  {"Rent Per SF":<12} {"Square Footage":<15} {"Annual Escalation":<17} {"Monthly Rent":<20} {"Annual Rent":<12} {"NNN Per SF":<10} {"Monthly NNN":<15} {"Gross Annual Rent":<15} {columns[9]:<15} {columns[10]:<22}')
            except:
                print(f'{"Lease Year":<7}  {"Rent Per SF":<12} {"Square Footage":<15} {"Annual Escalation":<17} {"Monthly Rent":<20} {"Annual Rent":<12} {"NNN Per SF":<10} {"Monthly NNN":<15} {"Gross Annual Rent":<15}')
            for i in rent_sheet:
                # formatting the table to align the columns for easier readability.
                try:
                    print(f'{i[0]:<7}     {i[1]:<12} {i[2]:<15} {i[3]:<17} {i[4]:<20} {i[5]:<12} {i[6]:<10} {i[7]:<15} {i[8]:<15}   {i[9]:<15} {i[10]:<22}')
                except:
                    print(
                        f'{i[0]:<7}     {i[1]:<12} {i[2]:<15} {i[3]:<17} {i[4]:<20} {i[5]:<12} {i[6]:<10} {i[7]:<15} {i[8]:<15}')
            print('▄' * 200)
            print('\nRent calculation table generated!\n')
            print('Disclaimer: Please note that this table is an estimate of the initial lease term and not to be relied upon. Please review the terms in your lease.\n')

        display_table()
            
    code_all = input('Press enter to continue.')
    if code_all == 'all':
        print('Secret Code initialized Successfully!')
        print('Running all programs...')
        calc_total_rent_paid()
        calc_landlord_concessions()
        try:
            fee = float(input('\nPlease enter a commission percentage paid to the brokerage (e.g., ".03" for 3%):'))
            calc_commission(fee)
        except:
            float_error()
        print('All functions completed successfully!')
    else:
        pass

    #User can select from different options depending on which number they enter.
    def main_menu():
        print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄')
        print('▌                                                                                                                                  ▌')
        print('▌                             ███    ███  █████  ██ ███    ██     ███    ███ ███████ ███    ██ ██    ██                            ▌')  
        print('▌                             ████  ████ ██   ██ ██ ████   ██     ████  ████ ██      ████   ██ ██    ██                            ▌') 
        print('▌                             ██ ████ ██ ███████ ██ ██ ██  ██     ██ ████ ██ █████   ██ ██  ██ ██    ██                            ▌') 
        print('▌                             ██  ██  ██ ██   ██ ██ ██  ██ ██     ██  ██  ██ ██      ██  ██ ██ ██    ██                            ▌') 
        print('▌                             ██      ██ ██   ██ ██ ██   ████     ██      ██ ███████ ██   ████  ██████                             ▌')
        print('▌                                                                                                                                  ▌') 
        print('▌                                                 Estimated Commercial Rent Sheet                                                  ▌')
        print('▌                                    Please select from the following options by their number:                                     ▌')
        print('▌                                                                                                                                  ▌')
        print('▌1. Show Entire Rent Sheet Table              2. Show Info from a Specific Lease Year               3. Calculate Broker Commission ▌')
        print('▌4. Create a New Table                        5. Get Total Rent Paid By Tenant                      6. Landlord Concessions Calc   ▌')
        print('▌7. Update Specific Item Data                 8. Update Column Data                                 9. Save Rent Sheet Table       ▌')
        print('▌10.Exit                                                                                                                           ▌')
        print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄')
        try:
            menu_answer = int(input('Please enter a number:\n'))
        except:
            integer_error()
        if menu_answer == 1:
            create_table.display_table()
            input('Press enter to continue...')
            main_menu()
        elif menu_answer == 2:
            try:
                year = int(input('\nPlease enter a lease year you would like to view:'))
                print('\n')
                show(year)
            except:
                integer_error()
        elif menu_answer == 3:
            try:
                fee = float(input('\nPlease enter a commission percentage paid to the brokerage (e.g., ".03" for 3%):'))
                calc_commission(fee)
            except:
                float_error()
        elif menu_answer == 4:
            main()
        elif menu_answer == 5:
            calc_total_rent_paid()
        elif menu_answer == 6:
            calc_landlord_concessions()
        elif menu_answer == 7:
            print(columns)
            create_table.display_table()
            try:
                column = float(input('[COL]\nPlease enter the column number index you would like to modify (First index "Lease Year" starts at 0):\n'))
                print(f'You\'ve selected column "{columns[int(column)]}".')
                row = float(input(f'[YEAR]\nPlease enter the lease year row item you would like to modify underneath "{columns[int(column)]}" column (First year index "1" is 1):'))
            except:
                float_error()
            create_table.update_item(row, column)
            create_table.display_table()
            main_menu()
        elif menu_answer == 8:
            print(columns)
            create_table.display_table()
            try:
                column = float(input('[COL]\nPlease enter the column number index you would like to modify (First index "Lease Year" starts at 0):'))
            except:
                float_error()
            create_table.update_column(column)
            create_table.display_table()
            main_menu()
        elif menu_answer == 9:
            # This code below adds the ability to save the estimated rent calculation sheet to a text file.
            save_file_question = input(
                f'\n(Type "yes" to save in both text and excel, "y" for only text, or "no" for none)\nWould you like to save the estimated rent sheet table to your computer?\n')
            if save_file_question.lower() in ('yes', 'y'):
                # Request the user to name the file
                name_file = input(f'What would you like to name the file as?')
                if save_file_question.lower() == 'yes':
                    # Convert the rent_sheet list to a DataFrame
                    try:
                        df = pd.DataFrame(rent_sheet, columns=columns)
                        # Save the DataFrame to an Excel file
                        df.to_excel(f'{name_file}.xlsx', index=False)
                        print(f'Your estimated rent sheet table have been saved as "{name_file}.xlsx"!')
                    except:
                        print(f'You do not have the pandas or openpyxl module installed in order to save the excel file.')
                        pass
                # Open a file to store the user's rent sheet table
                with open(f'{name_file}.txt', 'a') as f:
                    # Write the table results to the file
                    f.write('Estimated Rent Calculation Table:')
                    f.write('\n')
                    f.write('+' + ('-' * 120) + '+' + '\n') # Generates a bar design above the table
                    # The code below is for formatting of the spacing of the data to look more presentable
                    try:
                        f.write(
                            f'{columns[0]:<10} {columns[1]:<10} {columns[2]:<10} {columns[3]:<10} {columns[4]:<10} {columns[5]:<10} {columns[6]:<10} {columns[7]:<10} {columns[8]:<10} {columns[9]:<10} {columns[10]:<10}')
                    except:
                        f.write(
                            f'{columns[0]:<10} {columns[1]:<10} {columns[2]:<10} {columns[3]:<10} {columns[4]:<10} {columns[5]:<10} {columns[6]:<10} {columns[7]:<10} {columns[8]:<10}')
                    f.write('\n')
                    for i in rent_sheet:
                        try:
                            f.write(
                                f'{i[0]:<10} ${i[1]:<10} {i[2]:<10}     {i[3]:<10}        ${i[4]:<10}  ${i[5]:<10} ${i[6]:<10}${i[7]:<9}  ${i[8]:<10}       {i[9]:<10}      ${i[10]:<10}')
                            f.write('\n')
                        except:
                            f.write(
                                f'{i[0]:<10} ${i[1]:<10} {i[2]:<10}     {i[3]:<10}        ${i[4]:<10}  ${i[5]:<10} ${i[6]:<10}${i[7]:<9}  ${i[8]:<10}')
                            f.write('\n')
                    f.write('+' + ('-' * 120) + '+' + '\n')# Generates a bar design below the table
                    f.write('\n')
                    write_base_rent_total = 0
                    write_gross_rent_total = 0
                    for i in rent_sheet:
                        write_base_rent_total += i[5] # Adds all the base rent the tenant paid in column 6 over the lease term
                        write_gross_rent_total += i[8] # Adds all the gross rent (includes triple net expenses) the tenant paid in column 9 over the lease term
                    f.write(f'\nThe total BASE RENT paid by the tenant is estimated to be ${round(write_base_rent_total, 2)}\n') # Prints out total and rounds it
                    f.write(f'The total GROSS RENT paid by the tenant is estimated to be ${round(write_gross_rent_total, 2)}\n') # Prints out total and rounds it
                    f.write('\n')
                    if write_ti: # If the user entered a Tenant improvement allowance amount previously, then the code below will be added to the text file
                        total_guaranty = 0
                        guaranty_count = write_guaranty
                        for i in rent_sheet:
                                if guaranty_count >= 1:
                                    total_guaranty += i[5]
                                    guaranty_count -= 1
                                elif guaranty_count < 1: # This is when the guaranty count is a number like .5
                                    total_guaranty += (i[5] * guaranty_count)
                                    guaranty_count = 0
                        def month_or_months(variable):
                            month_string = 'month  '
                            if variable > 1:
                                month_string = month_string.strip()
                                month_string += 's '
                            return month_string
                        f.write(f'Tenant Allowance:  ${write_ti} per SF  (${write_ti * sf})\n')
                        f.write(f'Rent Abatement:    {write_free_rent} {month_or_months(write_free_rent)} (${round(write_free_rent * rent_sheet[0][4], 2)} not including NNN)\n')
                        f.write(f'Lease Guaranty:    {write_guaranty} year{"s" if write_guaranty > 1 else " "}   (${round(total_guaranty, 2)})\n')
                        f.write(f'Security Deposit:  {write_deposit} {month_or_months(write_deposit)} (${round((rent_sheet[0][4] + rent_sheet[0][7]) * write_deposit, 2)} including NNN)\n')
                    f.write('\n')
                    if write_broker_commission: # If the user entered a broker commission amount previously, then the code below will be added to the text file
                        total_commission = write_broker_commission + write_company_commission
                        f.write(f'Total Commission Paid to Brokerage: ${round(total_commission, 2)}\n')
                        f.write(f'Agent Commission ({round(100 * (write_broker_commission / total_commission), 2)}%): ${write_broker_commission}\n')
                        f.write(f'Company Split ({round(100 * (write_company_commission / total_commission), 2)}%): ${write_company_commission}\n')
                    f.write('\nDisclaimer: Please note that this table is an estimate of the initial lease term and not to be relied upon. Please review the terms in your lease.\n')
                    f.write('\n')
                    input(
                        f'\n(You can locate the file in your current folder directory where this program is saved)\nYour estimated rent sheet table have been saved as "{name_file}.txt"!\n')
            main_menu()
        elif menu_answer == 10:
            print('\nYou have successfully exited the program.')
            try:
                exit_main()
            except:
                take_care()
        else:
            print('The number you entered is not valid. Please try again.')
            main_menu()
    
    main_menu()
main()

# Exit function to close the program.
def exit():
    pass