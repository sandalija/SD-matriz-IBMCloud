from COS_backend import COS_backend

cos = COS_backend()


def main(args):
    bucket = 'deposit-sd-2020'  
    data = cos.get_object(bucket, args[0])
    # name = args.get("name", "pom")
    return {"file_content": data}

main('prova.txt')

