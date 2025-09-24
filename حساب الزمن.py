t_seconds =int(input('please enter number seconds\n'))
hours =t_seconds // 3600                     
minutes =(t_seconds%3600)/ 60                  
seconds = t_seconds % 60              
print(f'{hours} hours\n{minutes} minutes\n({seconds} seconds')
