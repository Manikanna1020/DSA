def hello(name,lang):
    greeting ={
        'English' : 'HELLO',
        'Spanish' : 'HELLO',
        'German' : 'HELLO'
    }
    msg =f'{greeting[lang]} {name}'
    print (msg)

if __name__ == '__main__':
    import argparse

    call = argparse.ArgumentParser(
        description='Please give me a cup '
    )

    call.add_argument(
        '-n','--name', metavar='name',
        required = True, help = 'give them a cup'
    )

    call.add_argument(
        '-l','-lang', metavar='language',
        required=True, choices=['English','Spanish','German'],
        help='The language of greeting'
    )

    args = call.parse_args()
     
hello(args.name,args.lang)