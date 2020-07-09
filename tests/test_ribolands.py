
# Build a ribolandscape based on different models and try the different algorithms.
import unittest
import matplotlib.pyplot as plt
import networkx as nx
from itertools import product, combinations, permutations
import RNA

from ribolands import RiboLandscape, PrimePathLandscape
from ribolands.parser import parse_barriers
from ribolands.pathfinder import clear_fpath_cache

A = """
    AAAGCCGCCUUAAGCCUACUUAGAUGGAAGUGACGUACGGGUAUUGGUACACGAUUUUAC
    ....(((.((.(((....))))).)))((((...((((........))))...))))...
    ................(((((......)))))..((((........))))..........
    ....(((.((.(((....))))).)))((((...((((........))))...))))...
    ...(((((((..(...((((........))))...)..))))...)))............
    ........(((.(.((((((((........))).))).)).))..)).............
    ....(((.(.((((....))))).)))((((...((((.(....).))))...))))...
    ....(((...((((....))))..))).......((((........))))..........
    ....(((...((((....))))..)))..((((.((((.(....).))))......))))
    ......((((......(((((......)))))......))))..((.....)).......
    ........((.(((....)))))...(((((...((((.(....).))))...)))))..
    ....((..((...((.(((((......)))))..))...))....)).............
    ....(((.(.((((....))))).))).......((((........))))..........
    ...((........))...(......)........((((.(....).))))..........
    ....(((.(.((((....))))).))).(((...((((........))))...)))....
    ...((((((....((.(((((......)))))..))...)))...)))............
    ....((...(((((....)))))..)).......((((........))))..........
    ...(((((((......(((((......)))))......))))...)))............
    ((((.((......(((.((((..(((.......)))..))))...)))...)).))))..
    ...((((((.((....(((((......)))))...)).))....))))............
    ....(((.((.(((....))))).)))((((...((((.(....).))))...))))...
    ...(((((((...((.(((((......)))))..))..)))...))))............
    ....(((..(((((....))))).)))((((...((((.(....).))))...))))...
    ...(((((((...((..((((......))))...))..))))...)))............
    ....(((.((.(((....))))).)))((((..(((((.(....).))))..)))))...
    ....((((..((((....))))).))).(((...((((........))))...)))....
    ...(((((((...((.(((((......)))))..))..))))...)))............
    ....((...(((((....)))))..)).......((((........))))..........
    .....((.((.(((....))))).))(((((...((((........))))...)))))..
    ....(((.(.((((....))))).))).......((((........))))..........
    .......(((...(.(..((.....))..)...)....)))...((...)).........
    ....(((.((..((....)).)).)))..((...((((........))))...)).....
    ....(((.(.((((....))))).))).(((...((((.(....).))))...)))....
    ....(((.((.(((....))))).))).(((...((((........))))...)))....
    .......(((((((....)))))..))((((...((((........))))...))))...
    .......(((((((....)))))..)).......((((.(....).))))..........
    .........(((((....)))))...(((((...((((........))))...)))))..
    ....((....((((....))))...)).......((((........))))..........
    ....((..((.(((....)))))..))((((...((((........))))...))))...
    ......(((.......(((((..(((.......)))..)))))..)))............
    ....(((...((((....))))..))).(((...((((........))))...)))....
    ....(((.((.(((....))))).)))..((...((((.(....).))))))........
    ....(((..(((((....))))).)))..((((.((.((.(((....))).)))).))))
    ...(((((((...((.((((........))))..))..))))...)))............
    ....(((.((.(((....))))).)))..(((...(((.(....).))))))........
    ....(((.((.(((....))))).))).......((((.(....).))))..........
    ......((((......(((((......)))))......))))((((.....)))).....
    ......((.....)).(((((......)))))..((((.(....).))))..........
    ......(((....(((((((((........))).))..))))...)))............
    ...(((((((...((.((((........))))..))..))))...)))............
    .....(((......((.........))..)))..((((........))))..........
    ....(((..(((((....))))).)))..(((((............)).)))(......)
    ...(((((((...((.(((((......)))))..))..))))...)))............
    ......(((.....((((((((........))).))).)).....)))............
    ...(((((((...(.(.(((........)))).)....)))...))))............
    ....(((.(.((((....))))).)))..(....((((........)))).)........
    ...(((((((..(...(((((......)))))...)..))))...)))............
    ...(((((((...(.(..(((......))).).)....)))...))))............
    ...(((((((...(..(((((......))))).)....))))...)))............
    ....(((..(((((....))))).)))((((...((((........))))...))))...
    ....(((.(.((((....))))).)))((((...((((........))))...))))...
    ....(((...((((....))))..))).(((...((((........))))...)))....
    .(((.(((.....)).(((((......)))))..((((.(....).))))..).)))...
    .......((.....((((((((........))).))).)).....)).............
    .......(((((((....)))))..)).(((...((((........))))...)))....
    ....(((..(((((....))))).))).......((((........))))..........
    .........(((((....))))).((((.(((...(((.(....).))))))...)))).
    ....(((.(.((((....))))).))).......((((........))))..........
    ...(((((((...(..(((((......))))).)....))))...)))............
    ...(((((((((.(..(((((......))))).).)).))))...)))............
    ....(((.(.((((....))))).)))..((...((((........))))...)).....
    .....((.(.((((....))))).))(((((...((((........))))...)))))..
    ...(((((((...(..(((((......)))))...)..))))...)))............
    ....(((.(.((((....))))).))).(((...((((........))))...)))....
    ...(((((((...((.((((........))))..))..))))...)))............
    ................(((((......)))))..((((.(....).))))..........
    ...(((((((...((.(((((......)))))..))..))))...)))............
    ....(((.(.((((....))))).))).......((((........))))..........
    ........(((..(.((....)).)..)))....((((........))))..........
    ...(((((((((.(..(((((......))))).).)).))))...)))............
    ....(((.((.(((....))))).)))((((...((((.(....).))))...))))...
    ....(((.((.(((....))))).))).......((((........))))..........
    ....(((.((.(((....))))).)))((((...((((........))))...))))...
    ...(((((((...((.(((((......)))))..))..))))...)))............
    ...((((.........(((((..(((.......)))..))))).))))............
    .....((......(((.((((..(((.......)))..))))...)))...)).......
    ....(((.((.(((....))))).)))((((...((((........))))...))))...
    ...(((((((.......(((........))).......))))...)))............
    ......(((....((((((((......))))).......)))...)))............
    ...(((((((...(.(.((((......))))).)....))))...)))............
    ...(((((((......(((((......)))))......))))...)))............
    ......((((......(((((......)))))......))))....((.....)).....
    ....(((.((.(((....))))).))).(((...((((........))))...)))....
    ...(((.(((((....(((((......)))))...)).)))....)))............
    ...(((((((......(((((......)))))......))))...)))............
    ....(((.((.(((....))))).))).......((((........))))..........
    ......(((....((((((((......))))).......)))...)))............
    ...(((((((......(((((......)))))......))))...)))............
    ...(((((((...(..(((((......))))).)....))))...)))............
    ....(((.(.((((....))))).)))..(((...(((........))))))........
    ....(((.(.((((....))))).)))((((...((((.(....).))))...))))...
""".split()

class TestRiboLandscape(unittest.TestCase):
    """
    Testing:

    A) Basic functions of RiboLandscape

        -) adding secondary structures (local minima)

    B) Rate model fitness (not a unittest....)

    """

    def setUp(self):
        pass

    def tearDown(self):
        clear_fpath_cache()

    def test_addnodes(self):
        vrna_md = RNA.md()
        vrna_md.temperature = 25
        seq = "AAAGCCGCCUUAAGCCUACUUAGAUGGAAGUGACGUACGGGUAUUGGUACACGAUUUUAC"
        RL = RiboLandscape(seq, vrna_md)
        RL.addnode('foo')
        assert RL.nodes['foo']['structure'] is None
        assert RL.nodes['foo']['energy'] is None
        assert RL.nodes['foo']['identity'] == 0

        ss = '....(((.((.(((....))))).)))((((...((((........))))...))))...' 
        en = -10.94
        RL.addnode('bar', structure = ss)
        assert RL.nodes['bar']['structure'] == ss
        assert RL.nodes['bar']['energy'] == en
        assert RL.nodes['bar']['identity'] == 1
        assert RL.nodes['bar']['occupancy'] == 0

        ss = '....(((.((.(((....))))).)))((((...((((........))))...))))...' 
        en = -10.94
        with self.assertRaises(AssertionError) as e:
            RL.addnode('hello', structure = ss, energy = '-9')
        with self.assertRaises(AssertionError) as e:
            RL.addnode('hello', structure = ss, energy = -9)

        RL.addnode(ss, structure = ss, energy = -9.0)
        assert RL.nodes[ss]['structure'] == ss
        assert RL.nodes[ss]['energy'] == -9.0
        assert RL.nodes[ss]['identity'] == 2
        assert RL.nodes[ss]['occupancy'] == 0

        RL.addnode(ss, structure = ss, energy = en, mynewatt = 15)
        assert RL.nodes[ss]['structure'] == ss
        assert RL.nodes[ss]['energy'] == en
        assert RL.nodes[ss]['identity'] == 3
        assert RL.nodes[ss]['occupancy'] == 0
        assert RL.nodes[ss]['mynewatt'] == 15

    def test_workflow(self):
        btree = """
              AGACGACAAGGUUGAAUCGCACCCACAGUCUAUGAGUCGGUGACAACAUU
            1 ..........((((.((((.((.((.......)).))))))..))))...  -6.70    0  13.00
            2 ..........((((.((((.((...((.....)).))))))..))))...  -6.10    1   2.10
            3 ..........((((.....((((.((.........)).)))).))))...  -5.90    1   6.30
            4 ((((.....(((........)))....))))....(((...)))......  -5.70    1   8.50
            5 ...((((...)))).....((((.((.........)).))))........  -5.60    3   4.80
            6 .(((......)))......((((.((.........)).))))........  -5.50    5   4.30
            7 ..........((((..((((.....((.....)).....))))))))...  -5.50    3   5.30
            8 ((((.....(((........)))....))))...................  -5.00    4   3.40
            9 ((((.....((.((.....))))....))))....(((...)))......  -5.00    4   2.80
           10 ((((.....((.((.....)).))...))))....(((...)))......  -4.90    4   3.50
        """
        brates = """ 1.177    0.02829  0.0006651  0.0001121  0.0002574  0.0005517    0.00037  6.188e-07  8.604e-08  8.272e-08 
                   0.09657     0.3762          0          0          0          0  5.296e-07          0          0          0 
                  0.002881          0      1.378  4.753e-07   0.004488      0.011   0.001809          0          0          0 
                  0.000405          0  3.967e-07      1.803  1.587e-06  1.319e-06  6.156e-07   0.009484   0.004989   0.002016 
                  0.000817          0   0.003289  1.394e-06       2.07   0.008785          0          0          0          0 
                  0.001792          0   0.008247  1.185e-06   0.008992      2.474          0          0          0          0 
                  0.001825  7.653e-07    0.00206    8.4e-07          0          0      2.378          0          0          0 
                 8.318e-06          0          0    0.03527          0          0          0      3.295          0          0 
                 1.759e-06          0          0    0.02822          0          0          0          0     0.6094   0.001226 
                  1.95e-06          0          0    0.01315          0          0          0          0   0.001413     0.7636 """

        vrna_md = RNA.md()
        lmins = parse_barriers(btree, is_file = False, return_tuple = True)

        RM = []
        for line in brates.split('\n'):
            RM.append(list(map(float, line.strip().split())))

        seq = lmins[0]
        RL = RiboLandscape(seq, vrna_md)

        # Import structures
        for lm in lmins[1:]: 
            RL.addnode(lm.id, structure = lm.structure, energy = lm.energy, identity = lm.id)

        # Import rates
        for i1, row in enumerate(RM, 1):
            for i2, val in enumerate(row, 1):
                if val != 0:
                    RL.add_edge(i1, i2, weight = val)

        # Print and plot output files
        RL.get_simulation_files_tkn('RL_test')
        RL.to_crn('RL_test.crn')
        RL.plot_to('RL_test.pdf', label = 'identity')

class TestPrimePathLandscape(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        clear_fpath_cache()

    def test_addnodes(self):
        vrna_md = RNA.md()
        vrna_md.temperature = 25
        seq = "AAAGCCGCCUUAAGCCUACUUAGAUGGAAGUGACGUACGGGUAUUGGUACACGAUUUUAC"
        RL = PrimePathLandscape(seq, vrna_md)
        RL.addnode('foo')
        assert RL.nodes['foo']['structure'] is None
        assert RL.nodes['foo']['energy'] is None
        assert RL.nodes['foo']['identity'] == 0

        ss = '....(((.((.(((....))))).)))((((...((((........))))...))))...' 
        en = -10.94
        RL.addnode('bar', structure = ss)
        assert RL.nodes['bar']['structure'] == ss
        assert RL.nodes['bar']['energy'] == en
        assert RL.nodes['bar']['identity'] == 1
        assert RL.nodes['bar']['active'] is None
        assert RL.nodes['bar']['lminreps'] is None
        assert RL.nodes['bar']['hiddennodes'] is None
        assert RL.nodes['bar']['occupancy'] == 0

        ss = '....(((.((.(((....))))).)))((((...((((........))))...))))...' 
        en = -10.94
        with self.assertRaises(AssertionError) as e:
            RL.addnode('hello', structure = ss, energy = '-9')
        with self.assertRaises(AssertionError) as e:
            RL.addnode('hello', structure = ss, energy = -9)

        RL.addnode(ss, structure = ss, energy = -9.0)
        assert RL.nodes[ss]['structure'] == ss
        assert RL.nodes[ss]['energy'] == -9.0
        assert RL.nodes[ss]['identity'] == 2
        assert RL.nodes[ss]['active'] is None
        assert RL.nodes[ss]['lminreps'] is None
        assert RL.nodes[ss]['hiddennodes'] is None
        assert RL.nodes[ss]['occupancy'] == 0

        RL.addnode(ss, structure = ss, energy = en, mynewatt = 15, 
                active = True, 
                hiddennodes = set())
        assert RL.nodes[ss]['structure'] == ss
        assert RL.nodes[ss]['energy'] == en
        assert RL.nodes[ss]['identity'] == 3
        assert RL.nodes[ss]['active'] is True
        assert RL.nodes[ss]['lminreps'] is None
        assert RL.nodes[ss]['hiddennodes'] == set()
        assert RL.nodes[ss]['occupancy'] == 0
        assert RL.nodes[ss]['mynewatt'] == 15

    def test_flooding_01(self):
        # 1) Read a bunch of local minima.
        # 2) Connect them with prime path flooding.
        # 3) Coarse grain the network.
        btree = """ # A barrier tree: minh = 3, max = 30, temperature = 25
            AAAGCCGCCUUAAGCCUACUUAGAUGGAAGUGACGUACGGGUAUUGGUACACGAUUUUAC
          1 ....(((.(.((((....))))).)))((((...((((........))))...))))... -10.94    0  12.00
          2 ....(((.((.(((....))))).)))((((...((((........))))...))))... -10.94    1   3.11
          3 ...(((((((......(((((......)))))......))))...)))............ -10.86    1   8.12
          4 ....(((.(.((((....))))).))).......((((........)))).......... -10.76    1   3.49
          5 ....(((.((.(((....))))).))).......((((........)))).......... -10.76    4   3.11
          6 ....(((.(.((((....))))).)))..((((.((.((.(((....))).)))).)))) -10.56    1   7.66
          7 ....(((.((.(((....))))).)))..((((.((.((.(((....))).)))).)))) -10.56    6   3.11
          8 ......(((...(.((((((((........))).))).)).)...)))............ -10.24    1   9.03
          9 .............((((((((..(((.......)))..)))))..)))............ -10.23    1   9.61
         10 ...((........)).(((((......)))))..((((........)))).......... -10.00    1   7.12
        """
        vrna_md = RNA.md()
        vrna_md.temperature = 25
        lmins = parse_barriers(btree, is_file = False, return_tuple = True)
        seq = lmins[0]

        PPL = PrimePathLandscape(seq, vrna_md)
        PPL.minh = 3

        # Construct the state-space as PrimePathLandscape graph:
        for lm in lmins[1:]: 
            PPL.addnode(lm.structure, 
                        structure = lm.structure, 
                        occupancy = 1/len(lmins[1:]), 
                        energy = lm.energy)

        print(f'\nInitial graph size: {len(PPL)}')

        nn = PPL.connect_nodes_n2()
        print(f'N2 connected graph size: {len(PPL)}, new: {len(nn)}')

        PPL.coarse_grain()
        print(f'After coarse graining: {len(PPL.active_nodes)} active,',
                                     f'{len(PPL.inactive_nodes)} hidden.')

        # Look at it!
        self.plot_active_subgraph(PPL, 'PPL_01_normal')

        PPL.get_simulation_files_tkn('PPL_01_normal')

        # Find the prime path transitions between two structures:
        ss2 = '....(((.((.(((....))))).)))((((...((((........))))...))))...'
        ss3 = '...(((((((......(((((......)))))......))))...)))............'
        #for x in PPL.get_prime_path_minima(ss3, ss2): print(x)

        # Now reduce the graph to the minimal graph where only 
        # ss2, ss3, and connecting basins are active.
        PPL.minimal_prime_path_graph(nodes = [ss2, ss3])

        # ... and then get the active subgraph.
        APL = PPL.active_subgraph
        APL.get_simulation_files_tkn('PPL_01_mini')
        APL.plot_to('PPL_01_mini.pdf', label = 'identity')
        APL.to_crnsimulator('PPL_01_simu')


    def test_flooding_02(self):
        # 1) Read a bunch of local minima.
        # 2) Connect them with prime path flooding.
        # 3) Coarse grain the network.
        btree = """ # A barrier tree: minh = 3, max = 30, temperature = 25
            AAAGCCGCCUUAAGCCUACUUAGAUGGAAGUGACGUACGGGUAUUGGUACACGAUUUUAC
         # 1 ....(((.(.((((....))))).)))((((...((((........))))...))))... -10.94    0  12.00
         # 2 ....(((.((.(((....))))).)))((((...((((........))))...))))... -10.94    1   3.11
         # 3 ...(((((((......(((((......)))))......))))...)))............ -10.86    1   8.12
         # 4 ....(((.(.((((....))))).))).......((((........)))).......... -10.76    1   3.49
         # 5 ....(((.((.(((....))))).))).......((((........)))).......... -10.76    4   3.11
         # 6 ....(((.(.((((....))))).)))..((((.((.((.(((....))).)))).)))) -10.56    1   7.66
         # 7 ....(((.((.(((....))))).)))..((((.((.((.(((....))).)))).)))) -10.56    6   3.11
         # 8 ......(((...(.((((((((........))).))).)).)...)))............ -10.24    1   9.03
         # 9 .............((((((((..(((.......)))..)))))..)))............ -10.23    1   9.61
         #10 ...((........)).(((((......)))))..((((........)))).......... -10.00    1   7.12
         11 ......((((......(((((......)))))......))))((((.....)))).....  -9.93    3   4.58
         12 ...((..(((((((....)))))..))..))...((((........))))..........  -9.82    1   4.11
         13 ......((.....)).(((((......)))))..((((........))))..........  -9.56   10   3.69
         14 ...((((.(((..((.(((((......)))))..))..)))...))))............  -9.55    3   5.62
         15 ((((.((......((((((((..(((.......)))..)))))..)))...)).))))..  -9.48    9   3.33
         16 .(((..((.....))...))).....(((((...((((........))))...)))))..  -9.36    1   4.19
         17 ...((........))...........(((((...((((........))))...)))))..  -9.30    1   4.08
         18 ....(((.(.((((....))))).)))..(((...(((........))))))........  -9.22    1   3.92
         19 ....(((.((.(((....))))).)))..(((...(((........))))))........  -9.22   18   3.11
         20 .......(((((((....)))))..))((((...((((........))))...))))...  -9.08    1   3.14
         21 ......(((....((((((((......)))).......))))...)))............  -9.08    8   7.11
         22 ....(((.(.((((....))))).)))..((((.((((........))))......))))  -9.06    1   5.34
         23 ....(((.((.(((....))))).)))..((((.((((........))))......))))  -9.06   22   3.11
         24 ....(((.(.((((....))))).)))..(((((............)).)))........  -8.91    1   3.87
         25 ....(((.((.(((....))))).)))..(((((............)).)))........  -8.91   24   3.11
         26 ......(((....(((((((((........))).))..))))...)))............  -8.86    8   4.76
         27 ...(((((.....)).(((((..(((.......)))..)))))..)))............  -8.77    9   5.51
         28 .......(((((((....)))))..))..((((.((.((.(((....))).)))).))))  -8.70    6   3.19
         29 ...(((((((...((((.((.....)).)).).)....))))...)))............  -8.57    3   5.16
         30 .........(((((....))))).(((((.....((((........))))....))))).  -8.50    1   4.19
        """

        # Input structures for debugging ...
        is1 = '....(((.(.((((....))))).)))((((...((((........))))...))))...'
        is2 = '....(((.((.(((....))))).)))((((...((((........))))...))))...'
        is3 = '...(((((((......(((((......)))))......))))...)))............'
        is4 = '....(((.(.((((....))))).))).......((((........))))..........'
        is5 = '....(((.((.(((....))))).))).......((((........))))..........'
        is6 = '....(((.(.((((....))))).)))..((((.((.((.(((....))).)))).))))'
        is7 = '....(((.((.(((....))))).)))..((((.((.((.(((....))).)))).))))'
        is8 = '......(((...(.((((((((........))).))).)).)...)))............'
        is9 = '.............((((((((..(((.......)))..)))))..)))............'
        is10= '...((........)).(((((......)))))..((((........))))..........'

        vrna_md = RNA.md()
        vrna_md.temperature = 25
        lmins = parse_barriers(btree, is_file = False, return_tuple = True)
        seq = lmins[0]

        PPL = PrimePathLandscape(seq, vrna_md)
        PPL.minh = 3

        # Construct the state-space as PrimePathLandscape graph:
        for lm in lmins[1:]: 
            PPL.addnode(lm.structure, structure = lm.structure, energy = lm.energy)

        print(f'\nInitial graph size: {len(PPL)}')

        nn = PPL.connect_nodes_n2()
        print(f'N2 connected graph size: {len(PPL)}, new: {len(nn)}')

        PPL.coarse_grain()
        print(f'After coarse graining: {len(PPL.active_nodes)} active,',
                                     f'{len(PPL.inactive_nodes)} hidden.')

        self.plot_active_subgraph(PPL, 'PPL_02_normal')

        # Unfortunately, this takes a long time, but you can set lim higher 
        # for more fine-grained results
        lim = 5
        while nn:
            be = [n for n in PPL.active_nodes if PPL.nodes[n]['energy'] < -8.50] 
            nn = PPL.connect_nodes_n2(nodes = be)
            print(f'New n2 connected graph size: {len(PPL)}, new: {len(nn)}')
            PPL.coarse_grain()
            print(f'After coarse graining: {len(PPL.active_nodes)} active,',
                                         f'{len(PPL.inactive_nodes)} hidden.')
            lim -= 1
            if not lim: break
        self.plot_active_subgraph(PPL, 'PPL_02_big')

        islist = []
        for e, x in enumerate([is1, is2, is3, is4, is5, is6, is7, is8, is9, is10], 1):
            if PPL.has_node(x):
                islist.append(x)
            else:
                print(f'Node {e} not found: {x}')

        PPL.minimal_prime_path_graph(nodes = islist)
        APL = PPL.active_subgraph
        APL.nodes[is6]['occupancy'] = 0.4
        APL.nodes[is10]['occupancy'] = 0.6
        APL.get_simulation_files_tkn('PPL_02_mini')
        self.plot_active_subgraph(PPL, 'PPL_02_mini')
        APL.plot_tkn('PPL_02_mini_simu.pdf', 
                APL.simulate_tkn('PPL_02_mini', t0 = 0.1, t8 = 1e9, force = True),
                ylim = (-0.02, 1.02))

    def plot_active_subgraph(self, L, name = 'test', form = 'pdf'):
        AL = L.active_subgraph
        print('Active subgraph size: {}'.format(len(AL)))
        for n in AL.sorted_nodes():
            print('{} {:6.2f} {:4d}'.format(n, AL.nodes[n]['energy'], AL.nodes[n]['identity']))

        grfile = f"{name}_graph.{form}"
        plt.subplot(111)
        labs = {a : b['identity'] for a, b in AL.nodes(data = True)}
        nx.draw_circular(AL, with_labels = True, labels = labs)
        plt.savefig(grfile)
        plt.close()
        print('# Printed file:', grfile)


if __name__ == '__main__':
    unittest.main()
