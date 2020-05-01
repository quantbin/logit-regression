# logit-regression
Logistic regression approximation of Covid19 death rate. Data is as of April 30, 2020. 

https://en.wikipedia.org/wiki/Logistic_function

Logistic regression can be used to model a number of processes, including the propagation of a virus. It describes the non-linear population growth:

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/cd66ce29a6e4c09182f3af05f1a3b67e6a7ce528)

with phase portrait:

<img src="https://github.com/quantbin/logit-regression/blob/master/img/logit-phase.gif" width="500">

and first derivative (density):

<img src="https://github.com/quantbin/logit-regression/blob/master/img/1024px-Logisticpdfunction.svg.png" width="500">

The accumulated number of Covid deaths in Italy follows similar pattern:

<img src="https://github.com/quantbin/logit-regression/blob/master/img/italy-fact.PNG?raw=true" width="500">

With daily number of deaths looking like:

<img src="https://github.com/quantbin/logit-regression/blob/master/img/italy-fact-hump.PNG?raw=true" width="500">

The problem is that if we try to fit the logit function in it, the fit will not be great:

![italy (one hump)](https://github.com/quantbin/logit-regression/blob/master/img/italy-1h.png?raw=true)

But if we fit a sum of two logit functions, the fit becomes much better:

![italy (two hump)](https://github.com/quantbin/logit-regression/blob/master/img/italy-2h.png?raw=true)

Same with Spain. One logit model:

![spain (one hump)](https://github.com/quantbin/logit-regression/blob/master/img/spain-1h.png?raw=true)

Two hump model:

![spain (two hump)](https://github.com/quantbin/logit-regression/blob/master/img/spain-2h.png?raw=true)

Germany - one hump vs two hump:

![germany (one hump)](https://github.com/quantbin/logit-regression/blob/master/img/germany-1h.png?raw=true)
![germany (two hump)](https://github.com/quantbin/logit-regression/blob/master/img/germany-2h.png?raw=true)

France:

![france (one hump)](https://github.com/quantbin/logit-regression/blob/master/img/france-1h.png?raw=true)
![france (two hump)](https://github.com/quantbin/logit-regression/blob/master/img/france-2h.png?raw=true)

Below are the two-hump models for few more countries:

![austria (two hump)](https://github.com/quantbin/logit-regression/blob/master/img/austria-2h.png?raw=true)
![belgium (two hump)](https://github.com/quantbin/logit-regression/blob/master/img/belgium-2h.png?raw=true)
![denmark (two hump)](https://github.com/quantbin/logit-regression/blob/master/img/denmark-2h.png?raw=true)
![dutch (two hump)](https://github.com/quantbin/logit-regression/blob/master/img/dutch-2h.png?raw=true)
![iran (two hump)](https://github.com/quantbin/logit-regression/blob/master/img/iran-2h.png?raw=true)
![israel (two hump)](https://github.com/quantbin/logit-regression/blob/master/img/israel-2h.png.png?raw=true)
![norway (two hump)](https://github.com/quantbin/logit-regression/blob/master/img/norway-2h.png?raw=true)
![portugal (two hump)](https://github.com/quantbin/logit-regression/blob/master/img/portugal-2h.png?raw=true)
![sweden (two hump)](https://github.com/quantbin/logit-regression/blob/master/img/sweden-2h.png?raw=true)
![swiss (two hump)](https://github.com/quantbin/logit-regression/blob/master/img/swiss-2h.png?raw=true)
![turkey (two hump)](https://github.com/quantbin/logit-regression/blob/master/img/turkey-2h.png?raw=true)
