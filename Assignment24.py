# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 22:14:44 2017

@author:Prathyusha Mallela
"""

#assignment 2.4
def format_string():
    print("The formated string of would be: ");
    s='{}WE, THE PEOPLE OF INDIA, {}{:>6}having solemnly resolved to constitute India into a SOVEREIGN, {}{}{:>12}SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC {}{:>13}and to secure to all its citizens{}'.format('','\n',' ','!','\n',' ','\n',' ',':');
    print(s);
    return s;

s=format_string();

