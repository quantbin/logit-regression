# Logistic regression approximation of Covid19 death rate. 

# Summary
Using two logit functions to approximate the death rate provides a very good fit for many countries, while single logit falls behind. 

Python Jupyter notebook code can be found in src folder. Data is as of April 30, 2020. 

# Intro

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

# Results

The problem is that if we try to fit the logit function in it, the fit will not be great:

![italy (one hump)](https://github.com/quantbin/logit-regression/blob/master/img/italy-1h.png?raw=true)

But if we fit a sum of two logit functions, the fit becomes much better:

![italy (two hump)](https://github.com/quantbin/logit-regression/blob/master/img/italy-2h.png?raw=true)

Same with Spain. One logit model:

![spain (one hump)](https://github.com/quantbin/logit-regression/blob/master/img/spain-1h.png?raw=true)

Two hump model:

![spain (two hump)](https://github.com/quantbin/logit-regression/blob/master/img/spain-2h.png?raw=true)


Portugal, on the other hand, doesn't fit well neither in one nor two hump models:

![portugal (two hump)](https://github.com/quantbin/logit-regression/blob/master/img/portugal-1h.png?raw=true)
![portugal (two hump)](https://github.com/quantbin/logit-regression/blob/master/img/portugal-2h.png?raw=true)

Germany - one hump vs two hump (two hump is slightly better):

![germany (one hump)](https://github.com/quantbin/logit-regression/blob/master/img/germany-1h.png?raw=true)
![germany (two hump)](https://github.com/quantbin/logit-regression/blob/master/img/germany-2h.png?raw=true)

France:

![france (one hump)](https://github.com/quantbin/logit-regression/blob/master/img/france-1h.png?raw=true)
![france (two hump)](https://github.com/quantbin/logit-regression/blob/master/img/france-2h.png?raw=true)

Norway:

![norway (one hump)](https://github.com/quantbin/logit-regression/blob/master/img/norway-1h.png?raw=true)
![norway (two hump)](https://github.com/quantbin/logit-regression/blob/master/img/norway-2h.png?raw=true)

Below are the two-hump models for few more countries:

![belgium (two hump)](https://github.com/quantbin/logit-regression/blob/master/img/belgium-2h.png?raw=true)
![denmark (two hump)](https://github.com/quantbin/logit-regression/blob/master/img/denmark-2h.png?raw=true)
![dutch (two hump)](https://github.com/quantbin/logit-regression/blob/master/img/dutch-2h.png?raw=true)
![israel (two hump)](https://github.com/quantbin/logit-regression/blob/master/img/israel-2h.png?raw=true)
![sweden (two hump)](https://github.com/quantbin/logit-regression/blob/master/img/sweden-2h.png?raw=true)
![swiss (two hump)](https://github.com/quantbin/logit-regression/blob/master/img/swiss-2h.png?raw=true)
![turkey (two hump)](https://github.com/quantbin/logit-regression/blob/master/img/turkey-2h.png?raw=true)

Iran's trajectory is quite complex for one or two humps:

![iran (two hump)](https://github.com/quantbin/logit-regression/blob/master/img/iran-2h.png?raw=true)

Same with Austria - the fit is not great:

![austria (two hump)](https://github.com/quantbin/logit-regression/blob/master/img/austria-2h.png?raw=true)

# Interpretation of results
In many cases the two-logit model provides a much better fit than one-logit model. One possible explanation can be that there are two parallel epidemics taking place either in different geographies (within the same country) or in two different population groups in the same location that do not interact with each other and posess different characteristics (mobility, infection rate etc). 

Taking Italy and Spain, for example, the first hump is tall and narrow, which indicates fast spread with high mortality rate - probably nursing homes. Second hump could be the general population:

![italy (two hump)](https://github.com/quantbin/logit-regression/blob/master/img/italy-2h.png?raw=true)

But in some countries (like Sweden) teh first hump is mild, while the second one is more prominent:

![sweden (two hump)](https://github.com/quantbin/logit-regression/blob/master/img/sweden-2h.png?raw=true)

# Conclusion
Each country develops its own pattern of virus spread. In some cases it can be approximated by single logit function, in many cases it takes two logit functions to provide a good fit. Some countries deveop a unique pattern that is hard to model.
