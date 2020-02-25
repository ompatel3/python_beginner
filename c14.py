# Learning python 5e page 227
# chapter 7 string fundementals
import sys
print('%s=%s' % ('spam', 42)) # Format expression
print('{0}={1}'.format('spam', 42)) # Format method
print('{}={}'.format('spam', 42)) # With autonumbering

#% expression can’t handle keywords, attribute references, and binary type codes
print('%s, %s and %s' % (3.14, 42, [1, 2])) # Arbitrary types
# 3 types of key words using %
print('My %(kind)s runs %(platform)s' % {'kind': 'laptop', 'platform': sys.platform},'My laptop runs win32')
print('My %(kind)s runs %(platform)s' % dict(kind='laptop', platform=sys.platform),'My laptop runs win32')
somelist = list('SPAM')
parts = somelist[0], somelist[-1], somelist[1:3]
print('first=%s, last=%s, middle=%s' % parts,"first=S, last=M, middle=['P', 'A']")

# Adding specific formatting
print('%-10s = %10s' % ('spam', 123.4567))
print('%(plat)10s = %(kind)-10s' % dict(plat=sys.platform, kind='laptop')) # keywords before num


# Floating-point numbers
print('%e, %.3e, %g' % (3.14159, 3.14159, 3.14159))
print('%f, %.2f, %06.2f' % (3.14159, 3.14159, 3.14159))
print('%x, %o' % (255, 255))


# %()-8 = {1():<8}  %()8={1():>8}
print('My {1[kind]:<8} runs {0.platform:>8}'.format(sys, {'kind': 'laptop'}))
'My %(kind)-8s runs %(plat)8s' % dict(kind='laptop', plat=sys.platform)


# Building data ahead of time in both
data = dict(platform=sys.platform, kind='laptop')
print('My {kind:<8} runs {platform:>8}'.format(**data))
#**data in the method call here is special syntax that
#unpacks a dictionary of keys and values into individual “name=value” keyword arguments
print('My %(kind)-8s runs %(platform)8s' % data)
print('{0:d}'.format(999999999999)) # using d method
print('{0:,d}'.format(999999999999)) # using ,d method
print('{:,.2f}'.format(296999.2567))
# from formats import commas, money
# # print('%s' % commas(999999999999))
# # print('%s %s' % (commas(9999999), commas(8888888)))
# # print('%s' % money(296999.2567))
# # print([commas(x) for x in (9999999, 8888888)])

print('{name} {job} {name}'.format(name='Bob', job='dev'))
print('%(name)s %(job)s %(name)s' % dict(name='Bob', job='dev'))
D = dict(name='Bob', job='dev')
print('{0[name]} {0[job]} {0[name]}'.format(D))
print('{name} {job} {name}'.format(**D))
print('%(name)s %(job)s %(name)s' % D)

print('%.2f' % 1.2345)
print('%.2f %s' % (1.2345, 99))

#Functions versus expressions: A minor convenience
def myformat(fmt, args): return fmt % args
print(myformat('%s %s', (88, 99)))
print(str.format('{} {}', 88, 99))
print('%(num)i = %(title)s' % dict(num=7, title='Strings'))
print('{num:d} = {title:s}'.format(num=7, title='Strings'))
print('{num} = {title}'.format(**dict(num=7, title='Strings')))

# string
import string
t = string.Template('$num = $title')
print(t.substitute({'num': 7, 'title': 'Strings'}))
print(t.substitute(num=7, title='Strings'))
print(t.substitute(dict(num=7, title='Strings')))


