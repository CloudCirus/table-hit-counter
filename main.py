from functools import lru_cache
import timeit

from pandas import read_excel


@lru_cache
def parse_table(table_path: str) -> list:
    columns = [
        'user_id',
        'doc_id',
    ]
    users_and_docs = read_excel(table_path, usecols=columns,
                                keep_default_na=False).to_dict(orient='records')
    return users_and_docs


def get_users_with_docs(all_users: list) -> list:
    users_with_docs = []
    for doc in all_users:
        if doc['doc_id'] != 'NULL':
            users_with_docs.append(doc['user_id'])
    return users_with_docs


def main() -> None:
    all_users = parse_table('test.xlsx')
    all_users_count = len(all_users)
    print(f'{all_users_count} - USER_ID all')

    users_with_docs = get_users_with_docs(all_users)
    users_with_docs_count = len(users_with_docs)
    print(f'{users_with_docs_count} - USER_ID with DOC_ID not NULL')

    unic_users = set(users_with_docs)
    unic_users_count = len(unic_users)
    print(f'{unic_users_count} - USER_ID unic')

    repeated_users = users_with_docs_count - unic_users_count
    print(f'{repeated_users} - USER_ID with more that 1 document')

    proportion = repeated_users / all_users_count * 100
    print(f'{proportion} - % inside all USER_ID')


if __name__ == '__main__':
    print(f'\nwork time: {timeit.timeit(main, number=1)}')
