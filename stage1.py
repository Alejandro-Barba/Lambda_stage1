from datetime import date,timedelta, datetime
  
  
# Returns the current local date
today = datetime.today()
print(today)


glpca = 'DP_01.2022_GLPCA.csv'
glpca_costos = 'DP_01.2022_GLPCA_COSTOS.csv'

splited_glpca= glpca.replace(".csv", "").lower().split('_')
splited_glpca1= glpca_costos.replace(".csv", "").lower().split('_')

print(splited_glpca)
print(splited_glpca_costos)

#Saves the last day in a variable
upload_day = datetime.now().day
print(upload_day)

#Check if the recibed file is the first file of the day

first_upload = False
hour = datetime.now().hour
if hour == 4:
    first_upload = True
else:
    False

print('the upload was at ' + str(hour) )

#check if the file is the glpca or glpca_costos

if ('glpca' in splited_glpca) and ('costos' not in splited_glpca):
    # If the file is glpca the next lines are triggered
    print('glpca')
    # Check if is the first upload of the day
    if first_upload == True:
        splited_glpca.insert(1,'_'+str(upload_day-1)+'.')
    else :
        splited_glpca.insert(1,'_'+str(upload_day)+'.')
    filename = ''.join(splited_glpca)
    filename = splited_glpca[0] + splited_glpca[1] + splited_glpca[2] + '_' + splited_glpca[3] + '.csv'
    print(filename)
elif ('glpca' in splited_glpca) and ('costos' in splited_glpca):
    # If the file is glpca_costos the next lines are triggered
    print('glpca_costos')
        # Check if is the first upload of the day
    if first_upload == True:
        splited_glpca.insert(1,'_'+str(upload_day-1)+'.')
    else :
        splited_glpca.insert(1,'_'+str(upload_day)+'.')
    splited_glpca.insert(1,'_'+str(upload_day)+'.')
    print(splited_glpca)
    filename = splited_glpca[0] + splited_glpca[1] + splited_glpca[2] + '_' + splited_glpca[3] +'_' + splited_glpca[4] + '.csv'
    print(filename)
else:
    print('error')