# uvtrick_example.py
from uvtrick import Env
from sklearn.datasets import make_regression

X, y = make_regression(n_samples=10_000, n_features=10, random_state=42)

def bench(X,y):
	from time import time
	from sklearn.decomposition import PCA
	tic = time()
	pca = PCA(n_components=2).fit(X,y)
	toc=time()
	return toc-tic

print("Running sckit-learn benchmarks")
for version in ("1.4", "1.5"):
	for i in range(4):
		timed = Env(f"scikit-learn=={version}").run(bench, X, y)
		print(version, timed)

# NOTE: Original video by koaning
# https://youtu.be/jXWIxk2brfk?t=295&si=MIBYD6N14sgAB2x0
