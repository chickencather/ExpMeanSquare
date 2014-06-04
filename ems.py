"""
Derive expected mean squares from a linear model in latex form.

Authors:
Geoff
Tom

"""
import re

class ExMeanSquare:
    def __init__(self, model, effect_type, n_levels):
        """ Args:
            model: a linear model in latex form
                E.g. r"\alpha_{j} + \beta_{k} + \pi_{i(j)} + \epsilon_{i(jk)}"
                Be sure to use a raw string!
            effect_type: a list of 'fixed' or 'random' for each model term.
            n_levels: a list of number of levels in each non-error term.
                len(n_levels) must equal len(model) - 1, since we don't
                need the number of levels of the error term.
        """

        # 1 - Write linear model
        # Error checking
        model_terms = [s.strip() for s in model.split('+')]
        if any([e not in 'fixed random' for e in effect_type]):
            raise(Exception('effect_type must be a list of "fixed"/"random".'))
        if not len(model_terms) == len(effect_type) == (len(n_levels) + 1):
            raise(Exception('Args must have the same length.'))

        # get the subcomponents of each term
        model_list = []
        # i = 0
        for i_term, term in enumerate(model_terms):
            # get the factor name
            factor_name = term[:term.index('_')] 
            # get all subscripts for a factor
            factor_sub = re.findall('{(.+?)}', term)
            # split subscripts into whether they're in parenthesis
            factor_sub = factor_sub[0].split('(')
            # get the subscripts not in parenthesis
            factor_sub_no_par = factor_sub[0]
            # get the subscripts in parenthesis if applicable
            if len(factor_sub) > 1:
                factor_sub_par = factor_sub[1].replace(')', '')
            elif len(factor_sub) == 1:
                factor_sub_par = ''
            # Get the number of levels
            if i_term == len(n_levels):
                lev = None
            else:
                lev = n_levels[i_term]
            term_dict = {'name': factor_name,
                         'n_levels': lev,
                         'subscripts_nopar': factor_sub_no_par,
                         'subscripts_par': factor_sub_par,
                         'effect_type': effect_type[i_term]}
            model_list.append(term_dict)

        # 2 - Construct a 2-way table
        # Table constructed from list of lists. Initialized as list of Nones.
        # Rows: each term of the model
        # Cols: each subscript present in the model
        rownames = model_terms
        colnames = set([term['subscripts_nopar'] for term in model_list])
        table = [[None for n in range(len(colnames))] \
                    for m in range(len(rownames))]

        # 3 - Fill in the numeric cells of the table
        for i_col, subscript in enumerate(colnames):
            for i_row, param in enumerate(rownames):
                cell = 'FILL_IN'
                if re.search('\(?.*' + subscript + '.*\)?', param): # inside ()     
                    cell = 1
                elif re.search(subscript + '.*\(', param): # outside ()
                    if model_list[i_row]['effect_type'] in 'fixed':
                        cell = 1
                    elif model_list[i_row]['effect_type'] in 'random':
                        cell = 0
                elif not re.search(subscript, param): # not in term
                        cell = model_list[i_row]['n_levels']
                table[i_row][i_col] = cell

        # 4 - Put together the variance terms.
        # For each row, make a list of variance terms that include all
        # subscript letters, inside or outside parentheses.
        # Let's output a list of lists.
        # For each term in the linear model, make a list of which of those
        # terms we'll have to include a variance for.


        # 5 - Multiply each of the variance terms by their appropriate
        # numbers in the numerical table we constructed in step three.


        # Save the output of this process.
        self.model = model
        self.model_list = model_list
        self.rownames = rownames
        self.colnames = colnames
        self.table = table

    def latex_table(self):
        """ Output a latex-formatted table of self.table.
        """
        pass