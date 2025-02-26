import seaborn as sns

mpg = sns.load_dataset('mpg')

mpg.info()

print(mpg.sample(5).to_string())

print(mpg[["horsepower"]].tail())

#마력이 높으면 기름을 많이 먹음
#horsepoewer에 결측치가 6개 존재함
#해결 방법 1. 6개의 결측치를 다른 값으로 넣음 2. 결측치를 보여주는 6개를 날려버리기.