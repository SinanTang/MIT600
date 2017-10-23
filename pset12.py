# 6.00 Problem Set 12
#

import numpy as np
import random
import pylab
from matplotlib.offsetbox import AnchoredOffsetbox, TextArea, VPacker


class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """


#
# PROBLEM 1
#

class SimpleVirus(object):
    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    def __init__(self, maxBirthProb, clearProb):
        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.

        maxBirthProb: Maximum reproduction probability (a float between 0-1)

        clearProb: Maximum clearance probability (a float between 0-1).
        """
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb

    def __str__(self):
        return 'SimpleVirus({}, {})'.format(self.maxBirthProb, self.clearProb)

    def doesClear(self):
        """
        Stochastically determines whether this virus is cleared from the
        patient's body at a time step.

        returns: Using a random number generator (random.random()), this method
        returns True with probability self.clearProb(?) and otherwise returns
        False.
        """
        ran = random.random()
        if ran < self.clearProb: return True
        else: return False

    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the SimplePatient and
        Patient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.

        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.
        """
        bprob = self.maxBirthProb * (1 - popDensity)
        parent_birth = self.maxBirthProb
        parent_clear = self.clearProb
        ran = random.random()
        if ran < bprob:
            return SimpleVirus(parent_birth, parent_clear)
        else:
            raise NoChildException

# v1 = SimpleVirus(0.9, 0.8)
# for i in range(5):
#     # print(v1.doesClear())
#     # if v1.reproduce(0.5) == NoChildException: print('exception caught')
#     # print(v1.reproduce(0.5))
#     try:
#         new = v1.reproduce(0.5)
#         # print(new)
#     except: print('exception')
    # print(new)


class SimplePatient(object):
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """
    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the  maximum virus population for this patient (an integer)
        """
        self.viruses = viruses
        self.maxPop = maxPop

    def __str__(self):
        return 'SimplePatient({}, {})'.format(len(self.viruses), self.maxPop)

    def getTotalPop(self):
        """
        Gets the current total virus population.

        returns: The total virus population (an integer)
        """
        return len(self.viruses)

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:

        - Determine whether each virus particle survives and updates the list
          of virus particles accordingly.

        - The current population density is calculated. This population density
          value is used until the next call to update()

        - Determine whether each virus particle should reproduce and add
          offspring virus particles to the list of viruses in this patient.

        returns: the total virus population at the end of the update (an
        integer)
        """
        current_viruses = self.viruses[:]
        for i in range(len(current_viruses)):
            v = current_viruses[i]
            # self.viruses = current_viruses
            # the virus gets cleared
            if v.doesClear():
                # remove from list
                # del current_viruses[i]
                current_viruses[i] = 0
            # the virus stays
            else:
                popDensity = len(current_viruses) / self.maxPop
                # try reproducing - how to choose the exception branch?
                try:
                    new_virus = v.reproduce(popDensity)
                    current_viruses.append(new_virus)
                except:
                    pass
                    # print('no child exception')

        viruses_updated = []
        for v in current_viruses:
            if v == 0: continue
            else: viruses_updated.append(v)

        self.viruses = viruses_updated

        return self.getTotalPop()



#
# PROBLEM 2
#

def problem2():
    """
    Run the simulation and plot the graph for problem 2 (no drugs are used,
    viruses do not have any drug resistance).

    Instantiates a patient, runs a simulation for 300 timesteps, and plots the
    total virus population as a function of time.
    """
    virus_list = []
    for i in range(100):
        virus = SimpleVirus(0.1, 0.05)
        virus_list.append(virus)
    patient = SimplePatient(virus_list, 1000)

    def run_sim(timestep):
        virus_pop_ls = [len(virus_list)]
        for i in range(timestep):
            virus_pop = patient.update()
            virus_pop_ls.append(virus_pop)

        # xVals = pylab.arange(1, timestep)
        pylab.plot(virus_pop_ls, label='SimpleVirus, SimplePatient')
        pylab.xlabel('Timestep')
        pylab.ylabel('Virus Population')
        pylab.legend()
        pylab.title('Simple Virus Simulation with no Drug Treatment\n{} Timestep'.format(timestep))

    run_sim(300)
    pylab.show()


# problem2()



#
# PROBLEM 3
#

class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    """
    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        """
        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.

        maxBirthProb: Maximum reproduction probability (a float between 0-1)

        clearProb: Maximum clearance probability (a float between 0-1).

        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'grimpex',False}, means that this virus
        particle is resistant to neither guttagonol nor grimpex.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.
        """
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb
        self.resistances = resistances
        self.mutProb = mutProb

    def __str__(self):
        return 'ResistantVirus({}, {}, {}, {})'.format(self.maxBirthProb, self.clearProb, self.resistances, self.mutProb)

    def getResistance(self, drug):
        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in Patient to determine how many virus
        particles have resistance to a drug.

        drug: the drug (a string).

        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """
        return self.resistances[drug]

    def reproduce(self, popDensity, activeDrugs):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient class.

        If the virus particle is not resistant to any drug in activeDrugs,
        then it does not reproduce. Otherwise, the virus particle reproduces
        with probability:

        self.maxBirthProb * (1 - popDensity).

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent).

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.

        For example, if a virus particle is resistant to guttagonol but not
        grimpex, and `self.mutProb` is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90%
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        grimpex and a 90% chance that the offspring will not be resistant to
        grimpex.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings).

        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.
        """
        resist = False
        for drug in activeDrugs:
            if self.resistances.get(drug, None): resist = True

        if resist or len(activeDrugs) == 0:
            bprob = self.maxBirthProb * (1 - popDensity)
            parent_birth = self.maxBirthProb
            parent_clear = self.clearProb
            parent_resist = self.resistances
            parent_mutProb = self.mutProb

            ran = random.random()
            if ran < bprob:
                for drug in parent_resist:
                    r = random.random()
                    val = parent_resist[drug]
                    if r < 1-parent_mutProb:
                        pass
                        # print('keep original resistance')
                    else:
                        parent_resist[drug] = not val
                        # print('switch resistance status')
                        # T/F alternate
                return ResistantVirus(parent_birth, parent_clear, parent_resist, parent_mutProb)
            else:
                raise NoChildException
        else: raise NoChildException


# virus_ls1 = []
# for i in range(100):
#     virus = ResistantVirus(0.1, 0.05, {'guttagonol': False}, 0.5)
#     virus_ls1.append(virus)
#
# n = 0
# for v in virus_ls1:
#     try:
#         print(v.reproduce(0.1 ,['guttagonol']))
#     except:
#         n += 1
#         # print('no child exception')
# print('exception number: ', n)



class Patient(SimplePatient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """
    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).

        viruses: the list representing the virus population (a list of
        ResistantVirus instances)

        maxPop: the  maximum virus population for this patient (an integer)
        """
        self.viruses = viruses
        self.maxPop = maxPop
        self.drugs = []

    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: list of drugs being administered to a patient is updated
        """
        if newDrug not in self.drugs:
            self.drugs.append(newDrug)

    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.

        returns: The list of drug names (strings) being administered to this
        patient.
        """
        return self.drugs

    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in
        drugResist.

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'grimpex'])

        returns: the population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        resistPop = []
        for v in self.viruses:
            resistAll = True
            for drug in drugResist:
                if not v.resistances.get(drug, 0): resistAll = False
            if resistAll:
                resistPop.append(v)
        return len(resistPop)

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:

        - Determine whether each virus particle survives and update the list of
          virus particles accordingly

        - The current population density is calculated. This population density
          value is used until the next call to update().

        - Determine whether each virus particle should reproduce and add
          offspring virus particles to the list of viruses in this patient.
          The listof drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces.

        returns: the total virus population at the end of the update (an
        integer)
        """
        current_viruses = self.viruses[:]
        activeDrugs = self.getPrescriptions()
        for i in range(len(current_viruses)):
            v = current_viruses[i]
            # the virus gets cleared
            if v.doesClear():
                # remove from list
                # del current_viruses[i]
                current_viruses[i] = 0
                # print('virus gets cleared! current virus list:', len(current_viruses))
            # the virus stays
            else:
                # len(current_viruses) changes
                current_virus_pop = update_virus_pop(current_viruses)
                popDensity = len(current_virus_pop) / self.maxPop
                # try reproducing
                try:
                    # this branch is not visited
                    new_virus = v.reproduce(popDensity, activeDrugs)
                    current_viruses.append(new_virus)
                    # print('new virus added! current virus list:', len(current_viruses))
                except:
                    pass
                    # print('no child exception')

        # viruses_updated = update_virus_pop(current_viruses)
        self.viruses = update_virus_pop(current_viruses)

        return self.getTotalPop()

def update_virus_pop(current_viruses):
    res = []
    for v in current_viruses:
        if v == 0: continue
        else: res.append(v)
    return res

# virus_ls = []
# for i in range(50):
#     virus = ResistantVirus(0.1, 0.05, {'guttagonol': False}, 0.5)
#     virus_ls.append(virus)
# patient = Patient(virus_ls, 1000)
#
# patient.addPrescription('guttagonol')

# print(patient.update())
# print(patient.update())
# print(patient.update())

# print('after update')
# for v in patient.viruses:
#     if v.resistances['guttagonol'] == True: print(v)

#
# PROBLEM 4
#

def problem4():
    """
    Runs simulations and plots graphs for problem 4.

    Instantiates a patient, runs a simulation for 150 timesteps, adds
    guttagonol, and runs the simulation for an additional 150 timesteps.

    total virus population vs. time  and guttagonol-resistant virus population
    vs. time are plotted
    """
    virus_ls = []
    for i in range(100):
        virus = ResistantVirus(0.1, 0.05, {'guttagonol':False}, 0.005)
        virus_ls.append(virus)
    patient = Patient(virus_ls, 1000)

    # timestep = 150
    def runTrial(timestep=150):

        virus_no_treatment = [len(virus_ls)]
        for i in range(timestep):
            virus_pop = patient.update()
            virus_no_treatment.append(virus_pop)

        xAxis = [0]*(timestep+1)
        for i in range(1,timestep+2):
            xAxis[i-1] = i
        pylab.plot(xAxis, virus_no_treatment, label='Virus before treatment')


        new_virus_ls = patient.viruses
        patient.addPrescription('guttagonol')
        virus_after_treatment = [len(new_virus_ls)]
        for i in range(150):
            virus_pop = patient.update()
            virus_after_treatment.append(virus_pop)

        for i in range(timestep+1, timestep*2+2):
            xAxis[i-(timestep+1)] = i
        pylab.plot(xAxis, virus_after_treatment, c='r', label='Virus after treatment')

        pylab.xlabel('Timestep')
        pylab.ylabel('Virus Population')
        pylab.legend()
        pylab.title('Resistant Virus Simulation with Drug Treatment\n{} Timestep'.format(timestep))

        # pylab.show()

    runTrial(150)

# problem4()


#
# PROBLEM 5
#

def problem5():
    """
    Runs simulations and make histograms for problem 5.

    Runs multiple simulations to show the relationship between delayed treatment
    and patient outcome.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).
    """
    virus_ls = []
    for i in range(100):
        virus = ResistantVirus(0.1, 0.05, {'guttagonol':False}, 0.005)
        virus_ls.append(virus)
    # patient = Patient(virus_ls, 1000)

    def runTrial(timestep=150):
        """a single trial under 4 conditions:
        timestep: 300, 150, 75, 0
        return: final virus population
        """
        # Be careful about the initial state of a variable!
        # patient should be moved inside the function, b/c it needs to start at baseline every trial
        patient = Patient(virus_ls, 1000)
        for i in range(timestep):
            patient.update()

        new_virus_ls = patient.viruses
        patient.addPrescription('guttagonol')
        virus_after = [len(new_virus_ls)]
        for i in range(150):
            virus_pop = patient.update()
            virus_after.append(virus_pop)
        return virus_after[-1]

    # for i in range(2,10):
    #     final = runTrial(150)
    #     print(final)

    def runSim(num_trials, timestep):
        # fig = pylab.subplot()
        pylab.figure()
        final_virus_pop_ls = []
        for i in range(num_trials):
            final_virus_pop = runTrial(timestep)
            # print('final virus population', final_virus_pop)
            final_virus_pop_ls.append(final_virus_pop)
            if i%50 == 0:
                print('Delay: {}, Trial: {}, Virus Population: {}'.format(timestep, i, final_virus_pop))

        cured = 0
        for i in final_virus_pop_ls:
            if i < 50: cured += 1
        cured_per = cured / len(final_virus_pop_ls)

        pylab.hist(final_virus_pop_ls)

        # changing the color of x/y labels
        # ybox0 = TextArea('Number of Patients', textprops=dict(color='y', size=12, rotation=90, ha='left', va='bottom'))
        # ybox = VPacker(children=[ybox0], align='bottom', pad=0, sep=5)
        # anchored_ybox = AnchoredOffsetbox(loc=8, child=ybox, pad=0, frameon=False,
        #                                   bbox_to_anchor=(-0.10, 0.3), bbox_transform=fig.transAxes,
        #                                   borderpad=0.)
        #
        # xbox0 = TextArea('Final Virus Population - {}% cured'.format(cured), textprops=dict(color='y', size=12, rotation=0, ha='left', va='bottom'))
        # xbox = VPacker(children=[xbox0], align='bottom', pad=0, sep=5)
        # anchored_xbox = AnchoredOffsetbox(loc=8, child=xbox, pad=0, frameon=False,
        #                                   bbox_to_anchor=(0.45, -0.13), bbox_transform=fig.transAxes, borderpad=0.)

        # fig.add_artist(anchored_ybox)
        # fig.add_artist(anchored_xbox)

        pylab.title('Final Virus Population with {} Time Step Delay'.format(timestep))
        pylab.xlabel('Final Virus Population - {}% cured'.format(cured_per))
        pylab.ylabel('Number of Patients')

    runSim(100, 0)
    runSim(100, 75)
    runSim(100, 150)
    runSim(100, 300)

    # pylab.show()

# problem5()


# virus_ls = []
# for i in range(100):
#     virus = ResistantVirus(0.1, 0.05, {'guttagonol':False}, 0.005)
#     virus_ls.append(virus)
# patient = Patient(virus_ls, 1000)

# def runTrial(timestep=150):
#     """a single trial under 4 conditions:
#     timestep: 300, 150, 75, 0
#     return: final virus population
#     """
#     virus_before = [len(virus_ls)]
#     for i in range(timestep):
#         virus_pop = patient.update()
#         # virus_before.append(virus_pop)
#
#     new_virus_ls = patient.viruses
#     patient.addPrescription('guttagonol')
#     virus_after = [len(new_virus_ls)]
#     for i in range(150):
#         virus_pop = patient.update()
#         virus_after.append(virus_pop)
#     final = virus_after[-1]
#     return final

# print(runTrial(300))


#
# PROBLEM 6
#

def problem6():
    """
    Runs simulations and make histograms for problem 6.

    Runs multiple simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    150, 75, 0 timesteps between adding drugs (followed by an additional 150
    timesteps of simulation).
    """
    virus_ls = []
    for i in range(100):
        virus = ResistantVirus(0.1, 0.05, {'guttagonol':False, 'grimpex':False}, 0.005)
        virus_ls.append(virus)

    def runTrial(timestep=150):
        """a single trial under 4 conditions:
        timestep: 300, 150, 75, 0
        return: final virus population
        """
        patient = Patient(virus_ls, 1000)
        for i in range(150):
            patient.update()
        patient.addPrescription('guttagonol')

        for i in range(timestep):
            patient.update()
        patient.addPrescription('grimpex')

        new_virus_ls = patient.viruses
        virus_after = [len(new_virus_ls)]
        for i in range(150):
            virus_pop = patient.update()
            virus_after.append(virus_pop)
        return virus_after[-1]

    def runSim(num_trials, timestep):
        pylab.figure()

        final_virus_pop_ls = []
        for i in range(num_trials):
            final_virus_pop = runTrial(timestep)
            final_virus_pop_ls.append(final_virus_pop)
            if i%5 == 0:
                print('Delay: {}, Trial: {}, Virus Population: {}'.format(timestep, i, final_virus_pop))

        cured = 0
        for i in final_virus_pop_ls:
            if i < 50: cured += 1
        cured_per = cured / len(final_virus_pop_ls)

        pylab.hist(final_virus_pop_ls)
        pylab.title('Final Virus Population with Two-Drug Treatment\n{} Time Step Delay\n{} Trials'.format(timestep, num_trials))
        pylab.xlabel('Final Virus Population - {}% cured'.format(cured_per))
        pylab.ylabel('Number of Patients')

    runSim(30, 0)
    runSim(30, 75)
    runSim(30, 150)
    runSim(30, 300)

    # pylab.show()

# problem6()



#
# PROBLEM 7
#

def sim_delay():
    """
    Run simulations and plot graphs examining the relationship between
    administration of multiple drugs and patient outcome.

    Plots of total and drug-resistant viruses vs. time are made for a
    simulation with a 300 time step delay between administering the 2 drugs and
    a simulations for which drugs are administered simultaneously.
    """
    virus_ls = []
    for i in range(100):
        virus = ResistantVirus(0.1, 0.05, {'guttagonol': False, 'grimpex': False}, 0.005)
        virus_ls.append(virus)

    def runTrial(timestep=300):
        """a single trial under 4 conditions:
        timestep: 300, 150, 75, 0
        return: final virus population
        """
        patient = Patient(virus_ls, 1000)
        virus_pop_ls = [len(virus_ls)]
        virus_resist_gut = [patient.getResistPop(['guttagonol'])]
        virus_resist_gri = [patient.getResistPop(['grimpex'])]
        virus_resist_all = [patient.getResistPop(['guttagonol', 'grimpex'])]

        def updates(n):
            for i in range(n):
                virus_pop = patient.update()
                virus_pop_ls.append(virus_pop)
                virus_resist_gut.append(patient.getResistPop(['guttagonol']))
                virus_resist_gri.append(patient.getResistPop(['grimpex']))
                virus_resist_all.append(patient.getResistPop(['guttagonol', 'grimpex']))

        updates(150)

        patient.addPrescription('guttagonol')

        updates(timestep)

        patient.addPrescription('grimpex')

        updates(150)

        return virus_pop_ls, virus_resist_gut, virus_resist_gri, virus_resist_all

    # def runSim(num_trials):
    #
    #     virus_pop_ls, virus_resist_gut, virus_resist_gri, virus_resist_all = runTrial()
    #     l1_tot = 0
    #     for i in num_trials:
    #         l1, l2, l3, l4 = runTrial()
    #         l1_tot += l1
    #
    #     virus_pop_ls = l1_tot / num_trials

    virus_pop_ls, virus_resist_gut, virus_resist_gri, virus_resist_all = runTrial()
    pylab.figure()
    pylab.plot(virus_pop_ls, label='Virus Population')
    pylab.plot(virus_resist_all, label='Virus resistant to both drugs')
    pylab.plot(virus_resist_gri, label='Virus resistant to grimpex')
    pylab.plot(virus_resist_gut, label='Virus resistant to guttagonol')
    pylab.legend()
    pylab.title('Virus Population Dynamics with 2 Drugs')
    pylab.xlabel('Time Step')
    pylab.ylabel('Virus Population')

    # pylab.show()

# sim_delay()


def sim_simul():
    virus_ls = []
    for i in range(100):
        virus = ResistantVirus(0.1, 0.05, {'guttagonol': False, 'grimpex': False}, 0.005)
        virus_ls.append(virus)

    def runTrial():
        """a single trial under 4 conditions:
        timestep: 300, 150, 75, 0
        return: final virus population
        """
        patient = Patient(virus_ls, 1000)
        virus_pop_ls = [len(virus_ls)]
        virus_resist_gut = [patient.getResistPop(['guttagonol'])]
        virus_resist_gri = [patient.getResistPop(['grimpex'])]
        virus_resist_all = [patient.getResistPop(['guttagonol', 'grimpex'])]

        def updates(n):
            for i in range(n):
                virus_pop = patient.update()
                virus_pop_ls.append(virus_pop)
                virus_resist_gut.append(patient.getResistPop(['guttagonol']))
                virus_resist_gri.append(patient.getResistPop(['grimpex']))
                virus_resist_all.append(patient.getResistPop(['guttagonol', 'grimpex']))

        updates(150)

        patient.addPrescription('guttagonol')
        patient.addPrescription('grimpex')

        updates(150)

        return virus_pop_ls, virus_resist_gut, virus_resist_gri, virus_resist_all

    virus_pop_ls, virus_resist_gut, virus_resist_gri, virus_resist_all = runTrial()
    pylab.figure()
    pylab.plot(virus_pop_ls, label='Virus Population')
    pylab.plot(virus_resist_all, label='Virus resistant to both drugs')
    pylab.plot(virus_resist_gri, label='Virus resistant to grimpex')
    pylab.plot(virus_resist_gut, label='Virus resistant to guttagonol')
    pylab.legend()
    pylab.title('Virus Population Dynamics with 2 Drugs')
    pylab.xlabel('Time Step')
    pylab.ylabel('Virus Population')

    # pylab.show()

sim_simul()

pylab.show()



#
# Problem 8: Patient Non-compliance
#
"""
In the Patient class, modify the method getPrescriptions(), 
add another parameter *prob* - 
the probablity the patient doesn't take the drug. 
prob is a float between .0 and 1.0 inclusive.

In getPrescriptions(), Use random.random() to model the condition 
whether the drug is in Patient.drugs or not.
So in update() method in Patient class, the variable activeDrugs 
will change accordingly.

"""
