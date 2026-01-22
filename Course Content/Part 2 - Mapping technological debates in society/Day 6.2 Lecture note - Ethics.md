# Ethics (Lecture Note)

*Lecturer: Benjamin Lipp*

## Introduction

**Normative ethics** explores what makes something morally right or good. It follows **three main traditions**: **consequentialism**, **deontology**, and **virtue ethics**. Each tradition has distinct assumptions about moral goodness, orienting our thinking differently.[^1] For instance, deontology emphasizes morally good *intentions* and adherence to *universal norms*, while consequentialism disregards intentions, focusing exclusively on *outcomes*. Virtue ethics shifts focus again, emphasizing that morality arises from cultivating a *virtuous character* essential for a good and meaningful life. Each tradition contains many variations of these more general ways of thinking. We call these *ethical theories*. In this lecture, we will exemplify each tradition by one corresponding theory: effective altruism (as an example of consequentialism), John Rawl's theory of justice (deontology), and care ethics (virtue ethics). Different ethical theories lead to varied conclusions about whether a technology is morally good or bad, not necessarily because they disagree on outcomes, but because their base assumptions and thus their reasoning differs.

So, why learn multiple ethical theories? The goal of this lecture is not to provide you with absolute moral judgments. **No single theory is objectively correct or complete**. You will see that each theory can run into problems, that is, lead to morally questionable outcomes. Learning to understand why these theories arrive at certain conclusions and why their reasoning has limits will teach you how to evaluate and critically reflect ethical arguments in the real world. For example, lifecycle assessment, which you learnt about in the first part of the course, uses a consequentialist framework that measures and quantifies outcomes. From a deontological or virtue ethics perspective, however, this approach may seem limited, it does not account for norms or virtues to build a liveable society, for example. Examining lifecycle assessment through multiple ethical lenses highlights its potential blind spots and limitations it has. **A responsible engineer knows about these limitations and can juggle multiple ethical perspectives simultaneously**, not relying on any single theory alone.

[^1]: These distinctions are object of philosophical debate. Ethical concepts, and as you will learn in this course, any knowledge, contain assumptions about the world that can be subject to contestation and change. This does not mean that they are arbitrary, but rather that no single categorisation can claim 'objectivity' outside of its scientific and social context. The goal of following the distinction proposed above is thus not to give you an objective account of how philosophical ideas have evolved but rather to sensitise you for the fact that different theories of the 'good' are based on different assumptions about the world. Learning to make these assumptions transparent and to reflect them is what this lecture is about.

---

## Consequentialism: Maximising Good Outcomes

Consequentialism determines morality exclusively based on outcomes. It holds that actions or rules are morally justified if they maximize overall utility – often defined as happiness, well-being, or welfare – for the greatest number of people. Utility describes a net good, that is, the difference between good and bad consequences of a given action. This perspective is especially appealing due to its straight-forward methodological approach: measuring and then weighing positive against negative consequences.

Consequentialism appears in two forms:

- **Act Consequentialism**: Evaluates each action by its immediate consequences.
- **Rule Consequentialism**: Assesses actions based on adherence to rules that generally produce the best overall outcomes.

**Effective Altruism** is a movement that draws on consequentialist thinking. It involves using quantitative metrics to determine how to maximize the good achieved with limited resources, with "good" often understood as preventing unnecessary deaths (e.g., measured as lives saved). It consists of two core projects: an intellectual project aiming to identify the most effective ways to benefit others, and a practical project of acting according to these findings. EA emphasizes cost-effectiveness, evidence-based decisions, cause-neutrality, and impartiality, striving to allocate resources to interventions that produce the greatest positive impact per unit of input. It does not necessarily prescribe moral obligations, but guides those committed to altruism toward doing it most effectively.

**Limitations:** One problem is how to define and operationalize utility. A broadly defined utility (e.g., general happiness) risks oversimplification, while more nuanced definitions (e.g., specific pleasures or pains) are complicated by significant variations across different contexts or situations. Further criticisms include its potential neglect of important moral concepts like individual rights, autonomy, privacy, and distributive justice. Its emphasis on quantifiable interventions also potentially blinds it to systemic change and structural injustices, possibly favouring privileged populations and leading to highly problematic outcomes for minorities. For example, if one could save six people's lives by transplanting the organs of two, purely consequentialist thinking would advocate for killing two innocent people for the sake of saving six.

---

## Deontology: Duties and Rights

Deontology, unlike consequentialism, grounds morality in adherence to fixed duties and rights, independently of outcomes. A classic example is Immanuel Kant's Categorical Imperative. It is *categorical* insofar as it should be applicable to any given situation. It has two major components:

- The **Universality Principle** posits to act according to maxims that could coherently become universal laws applicable to all. In other words, act only in ways you could rationally endorse everyone acting in the same situation.
- The **Humanity Principle** posits that we should never treat other humans exclusively as means to an end (i.e., as instruments for achieving our own goals), and thus all people should be respected because of their inherent value as persons.

**John Rawl's Theory of Justice** develops deontological principles through hypothetical agreements among rational, impartial actors. It is thus often called a social contract theory, because these principles do not stem from a state of nature but from a collective agreement among individuals. Rawls advocates for fairness through the idea of the **Veil of Ignorance**, where individuals decide on rules without knowing their personal characteristics. This leads to principles safeguarding equal rights and justice, particularly the **Greatest Equal Liberty Principle**, protecting freedoms as long as they don't infringe on others' rights, and the **Difference Principle**, permitting inequalities only if benefiting society's least advantaged.

**Limitations:** Deontological ethics can be overly rigid, especially when different duties collide. For example, take the situation of someone who is hiding a persecuted minority in their house. When the police come looking for them, should they lie to the police (thus breaking the rule not to lie) or tell the policy (thus harming the people they house)? There are different responses to this problem (e.g., a hierarchy of duties), but in general, the problem persists that deontological ethics emphasizes universally applicable principles abstracted from context, which can overlook important relational, cultural, or situational nuances critical in evaluating specific situations.

---

## Virtue Ethics: Character and the Good Life

Virtue ethics diverges from evaluating specific actions or rules and instead emphasises the cultivation of a virtuous character which is seen as essential for a good and meaningful life. Virtues represent balanced character traits situated between extremes of deficiency and excess – such as courage situated between cowardice and recklessness. Virtue ethics thus encourages continuous self-improvement through practical experience and reflection. An example for this are professional codes of conduct for engineers, such as the Ingeniørforeningen i Danmark (IDA). It says that engineers should "[r]eflect on and be transparent about the societal, environmental, and ecological impacts of their work and the products or services they develop (and) [i]nvolve affected stakeholders in decision-making where possible, and lend their expertise to broader public debates on technology (IDA 2022).

**Care Ethics** can be subsumed under Virtue Ethics[^2], and challenges core assumptions of the other traditions in a specific way. Both consequentialism and deontology construct the 'good' in the abstract, either through calculation or generalisation. As a result, they run into problems when confronted with concrete situations (see discussions of limitations above). Instead, Care Ethics from the premise that giving and receiving care is a fundamental condition of human existence. Everyone at some points in their life needs care. Hence, Care Ethics constructs ethical responsibilities from how people (especially women) relate with *particular* others that they care for, e.g., their child or elderly parent. It recognises interdependence as a fundamental human condition, challenging the dominant 'liberal' paradigm centred on individual autonomy and universal justice. Understood as a type of Virtue Ethics, care is a motivational attitude built on responding to someone else's needs.

For the context of engineering, this means that Care Ethics emphasises the importance of empathy, sensitivity, and responsiveness to others' needs. It draws attention to asymmetrical power relations between engineers and end-users, who may be negatively affected by or excluded from technology. According to Care Ethics, engineers have a responsibility to anticipate and safeguard against negative consequences for vulnerable users, by engaging with and being attentive to people's own needs. Care Ethics may also evaluate the impact of technology on interpersonal relationships, for example, the moral distance created by systems of algorithmic decision-making (see Further Readings).

**Limitations:** While Virtue Ethics provides valuable insights into (inter)personal moral and professional development, it is also limited in clearly guiding decisions about more complex societal issues that go beyond the reach of an individual's actions. Additionally, critics argue that a focus on virtues may mistake culturally or context-specific norms for rigorous ethical standards. In particular, what might be viewed as appropriate and caring within a given context, could be viewed as problematic by outsiders (e.g., nepotism). Finally, a Care Ethics perspective has been criticised for positioning 'feminine' virtues of compassion against 'masculine' virtues of universality or rationality. This may reinforce gender norms rather than supporting Feminist causes.

[^2]: Although this categorisation is controversial. Some argue that care ethics denotes its own tradition that is distinctly different from any of the other traditions outlined here (the paper on Care Ethics in the Further Reading section below makes this argument). What most philosophers agree with, though, is that it represents a decidedly anti-consequentialist and anti-deontological way of thinking. Especially, early writings about Care Ethics explicitly position it as promoting "feminine" virtues that challenge "masculinist" assumptions in deontology and consequentialist thought.

---

## Further Readings

### For a general introduction into normative ethics in relation to technology:

Tsou JY and Walsh KP (2025) Ethical Theory and Technology. In: *Technology Ethics: A Philosophical Introduction and Readings*. New York: Routledge. Pre-Print. Available at: https://philpapers.org/archive/TSOETA.pdf

### For more in-depth discussions of specific ethical theories:

**On Effective Altruism and its role in development aid:** Jacobs B (2022) Is Effective Altruism Neocolonial? (an overview of the arguments and counterarguments). Available at: https://forum.effectivealtruism.org/posts/48Wr4jd7pooKsMzke/is-effective-altruism-neocolonial-an-overview-of-the

**A Rawl's Theory of Justice take information technology:** Hoffmann AL (2022) Rawls, Information Technology, and the Sociotechnical Bases of Self-Respect. In: Vallor S (ed.) *The Oxford Handbook of Philosophy of Technology*. Oxford handbooks online. New York: Oxford University Press, pp. 231–249.

**A Care Ethics discussion of algorithmic decision making:** Villegas-Galaviz C and Martin K (2024) Moral distance, AI, and the ethics of care. *AI & Society* 39(4): 1695–1706.
