# مشروع حساب الثواني إلى ساعات ودقايق وثواني
t_seconds =int(input('please enter number seconds\n'))

hours = t_seconds // 3600             
elbage= t_seconds % 3600           
minutes = elbage// 60                  
seconds = elbage% 60   
           
print(f'{hours} hours')
print(f'{minutes} minutes')
print(f'{seconds} seconds')