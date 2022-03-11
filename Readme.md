# Epstein Civil Violence Model
### Adaptation by Bruno Sanguinetti R. de Barros
### Universidade de Brasília - Computação Experimental

## Causal Hypothesis
## Hipóstese Causal

From the model and agent base, it is assumed that a predisposing factor in agents, this factor is a random number between 0.01 and 0.2 that is added to Grievance to increase or decrease the chance of a citizen joining the rebellion as an active member. . The bias factor can be dynamically modified by the interface, increasing or decreasing the factor.

The predisposition can represent social, economic or environmental factors that incline the agent to a certain posture during the simulation. The values ​​referring to the density of citizens, police officers and the legitimacy of the current political regime can also be changed.

Changes in predisposing factors significantly influence the number of active rebels during the simulation. However, the most important factor for a mass rebellion is the legitimacy of the current political regime.

A partir do modelo e agente base, assume-se que um fator de predisposição nos agentes, este fator é um número aleatório entre 0.01 e 0.2 que se soma ao Grievance para aumentar ou diminuir a chance de um cidadão se juntar a rebelião como membro ativo. O fator de predisposição pode ser modificado dinamicamente pela interface, aumentando ou diminuindo o fator.

A predisposição pode representar fatores sociais, econômicos ou ambientais que inclinam o agente a certa postura durante a simulação. Também podem ser alterados os valores referente a densidade de cidadãos, policiais e a legitimidade do regime político vigente.

As mudanças nos fatores de predisposição influenciam de forma considerável o número de rebeldes ativos durante a simulação. Porem o fator que mais pesa para uma rebelião em massa é a legitimidade do regime político vigente.

``self.grievance = self.hardship * (1 - self.regime_legitimacy - pre_condition[0])``

## Summary

This model is based on Joshua Epstein's simulation of how civil unrest grows and is suppressed. Citizen agents wander the grid randomly, and are endowed with individual risk aversion and hardship levels; there is also a universal regime legitimacy value. There are also Cop agents, who work on behalf of the regime. Cops arrest Citizens who are actively rebelling; Citizens decide whether to rebel based on their hardship and the regime legitimacy, and their perceived probability of arrest.

The model generates mass uprising as self-reinforcing processes: if enough agents are rebelling, the probability of any individual agent being arrested is reduced, making more agents more likely to join the uprising. However, the more rebelling Citizens the Cops arrest, the less likely additional agents become to join.

## How to Run
## Como executar
To run the model interactively, run ``run.py`` in this directory. e.g.
Para roda o modelo de forma iterativa, execute ``run.py`` no diretorio.

```
    $ python3 run.py
```

Then open your browser to [http://127.0.0.1:8521/](http://127.0.0.1:8521/) and press Reset, then Run.
Então abra seu navegador em [http://127.0.0.1:8521/](http://127.0.0.1:8521/) e selecione Start ou Reset.

## Files

* ``EpsteinCivilViolence.py``: Core model and agent code.
* ``EpsteinCivilViolenceServer.py``: Sets up the interactive visualization.
* ``Epstein Civil Violence.ipynb``: Jupyter notebook conducting some preliminary analysis of the model.

## Further Reading

This model is based adapted from:

[Epstein, J. “Modeling civil violence: An agent-based computational approach”, Proceedings of the National Academy of Sciences, Vol. 99, Suppl. 3, May 14, 2002](http://www.pnas.org/content/99/suppl.3/7243.short)

A similar model is also included with NetLogo:

Wilensky, U. (2004). NetLogo Rebellion model. http://ccl.northwestern.edu/netlogo/models/Rebellion. Center for Connected Learning and Computer-Based Modeling, Northwestern University, Evanston, IL.
