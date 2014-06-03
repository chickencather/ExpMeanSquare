"""
Derive expected mean squares from a linear model in latex form.

Authors:
Geoff
Tom

"""
import re

class ExMeanSquare:
    def __init__(self, model, fx_type):
        # Takes 2 arguments: a linear model in latex form and
        # a list containing a 'fixed' or 'random' entry for each model term

        # 1 - Write linear model
        # This is a latex model of the parameters of interest, of the form:
        # alpha_{j} + beta_{k} + pi_{i(j)} + epsilon_{i(jk)}
        # Be sure to use a raw string -- r"\alpha + \whatever"
        print model

        # make a dictionary to store info for each model term
        model_dict = {}

        # split up the model into each of the terms
        model_terms = [s.strip() for s in model.split('+')]

        # get the subcomponents of each term
        i = 0
        for term in model_terms:
            # create index to refer to model terms
            term_number = 'term_' + str(i+1)
            # get the factor name
            factor_name = term[:term.find('_')] 
            # get all subscripts for a factor
            factor_sub = re.findall('{(.+?)}', term)
            # split subscripts into whether they're in parenthesis
            factor_sub = factor_sub[0].split('(')
            # get the subscripts not in parenthesis
            factor_sub_no_par = list(factor_sub[0])
            # get the subscripts in parenthesis if applicable
            if len(factor_sub) > 1:
                factor_sub_par = list(factor_sub[1].replace(')', ''))
            elif len(factor_sub) == 1:
                factor_sub_par = ['']

            # add everything to the dictionary
            model_dict[term_number] = {'name': factor_name,
                                        'subscripts_nopar': factor_sub_no_par,
                                        'subscripts_par': factor_sub_par,
                                        'effect_type': fix_list[i]}
            i +=1

        # 2 - Construct a 2-way table
        # Table constructed from list of lists.
        # Rows: each term in the model
        # Cols: each subscript in the model
        rownames = [s.strip() for s in model.split('+')]
              
        # get all the subscripts
        all_subscripts = []
        # extract the subscripts for each term
        for key in model_dict.keys():
            all_subscripts.extend(model_dict[key]['subscripts_nopar'])
            all_subscripts.extend(model_dict[key]['subscripts_par'])

        # get rid of empty strings
        all_subscripts = filter(None, all_subscripts)
        # reduce to unique subscripts and sort them
        sorted(set(all_subscripts))

        # set the colnames
        colnames = all_subscripts

        table = [[None] * len(colnames)] * len(rownames)

        # 3 - Fill in the cells of the table
        for i_col, subscript in enumerate(colnames):
            for i_row, param in enumerate(rownames):
                cell = 'FILL_IN'
                table[i_row][i_col] = cell

        # 4 - blah blah

        # 5 - blah blah

        self.model = model
        self.table = table

    def latex_table(self):
        """ Output a latex-formatted table of self.table.
        """
        pass