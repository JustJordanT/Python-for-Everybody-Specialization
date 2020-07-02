# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    json2.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: JustJordanT <Jordantay9014@gmail.com>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/07/01 08:33:01 by JustJordanT       #+#    #+#              #
#    Updated: 2020/07/02 06:42:42 by JustJordanT      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import json

data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''

info = json.loads(data)
print('User count:', len(info))

for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])