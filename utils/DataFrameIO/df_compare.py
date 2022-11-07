"""
platform: any
env: any
name: df_compare.py
compare 2 dataframes
"""
import pandas as pd
import os


def strict_compare(df_1, df_2):
    """

    :param df_1:
    :param df_2:
    :return:
    """
    return df_1.compare(df_2)


def tuple_compare(tup_1, tup_2):
    """

    :param tup_1:
    :param tup_2:
    :return:
    """
    df_1 = pd.DataFrame(tup_1)
    df_2 = pd.DataFrame(tup_2)
    return strict_compare(df_1, df_2)


if __name__ == '__main__':
    # df = pd.read_csv("D:\\AlexYu\\more\\Ligand.csv")
    # sdf = pd.read_csv("D:\\AlexYu\\more\\SLigand.csv")
    # print(strict_compare(df, sdf))
    tup_mini = (13.327070671968617, -4.612279082387773, 13.327070671968617, 0.2964236093461592, -666, 456.4799999999999, 436.3200000000003, 456.1109039399105, 167, 1.4375, 2.25, 2.9375, 2.2254589298319036, 1968.2819307713883, 40.80651840778637, 35.14659241524687, 15.9630889961746, 23.159272603484283, 17.789881532605172, 8.71195092253299, 5.350003053578738, 6.349073820341519, 3.224024861657455, 4.182816929740727, 1.983504327965305, 2.650862037691216, -0.05000000000000005, 10.514999858276763, 12.074720419362798, 7.223145180609779, 215.24611471754955, 214.22255382280017, 61.87397117560682, 46.71735825643366, 0.0, 10.209723084138854, 4.992404732635669, 25.615634388304084, 13.47268658459819, 51.34077560108303, 0.0, 20.5082976248875, 0.0, 0.0, 11.761884949391115, 59.345962090840864, 19.178148736287287, 0.0, 44.27139593101842, 56.333180333718694, 2.8236841566564013, 0.0, 156.0, 135.59429296516672, 29.3912035259687, 0.0, 16.74731443130883, 0.0, 0.0, 0.0, 0.0, 0.0, 4.992404732635669, 27.497338167720358, 159.92584080732564, -0.38069215439976634, 51.021571568703955, 19.79968515505308, -2.5387799600807437, -11.135541414970291, -11.418077999191851, -8.987877947303584, -10.952794721803109, 0.0, 0.2857142857142857, 32, 2, 10, 1, 2, 3, 0, 0, 0, 9, 2, 11, 11, 0, 0, 0, 3, -3.220199999999995, 112.38740000000003, 2, 0, 0, 0, 0, 0, 0, 2, 2, 4, 4, 0, 0, 1, 2, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 4, 2, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0)
    tup_orig = (13.327070671968617, -4.612279082387773, 13.327070671968617, 0.2964236093461592, -666, 456.4799999999999, 436.3200000000003, 456.1109039399105, 167, 1.1875, 2.0, 2.6875, 2.2254589298319036, 1968.2819307713883, 40.80651840778637, 35.14659241524687, 15.9630889961746, 23.159272603484283, 17.789881532605172, 8.71195092253299, 5.350003053578738, 6.349073820341519, 3.224024861657455, 4.182816929740727, 1.983504327965305, 2.650862037691216, -0.05000000000000005, 10.514999858276763, 12.074720419362798, 7.223145180609779, 215.24611471754955, 214.22255382280017, 61.87397117560682, 46.71735825643366, 0.0, 10.209723084138854, 4.992404732635669, 25.615634388304084, 13.47268658459819, 51.34077560108303, 0.0, 20.5082976248875, 0.0, 0.0, 11.761884949391115, 59.345962090840864, 19.178148736287287, 0.0, 44.27139593101842, 56.333180333718694, 2.8236841566564013, 0.0, 156.0, 135.59429296516672, 29.3912035259687, 0.0, 16.74731443130883, 0.0, 0.0, 0.0, 0.0, 0.0, 4.992404732635669, 27.497338167720358, 159.92584080732564, -0.38069215439976634, 51.021571568703955, 19.79968515505308, -2.5387799600807437, -11.135541414970291, -11.418077999191851, -8.987877947303584, -10.952794721803109, 0.0, 0.2857142857142857, 32, 2, 10, 1, 2, 3, 0, 0, 0, 9, 2, 11, 11, 0, 0, 0, 3, -3.220199999999995, 112.38740000000003, 2, 0, 0, 0, 0, 0, 0, 2, 2, 4, 4, 0, 0, 1, 2, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 4, 2, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0)
    print(tuple_compare(tup_orig, tup_mini))
