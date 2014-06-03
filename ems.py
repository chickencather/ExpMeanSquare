"""
Derive expected mean squares from a linear model in latex form.
"""

class ExMeanSquare:
    def __init__(self, model):

        # 1 - Write linear model
        # This is a latex model of the parameters of interest, of the form:
        # alpha_{j} + beta_{k} + pi_{i(j)} + epsilon_{i(jk)}
        # Be sure to use a raw string -- r"\alpha + \whatever"
        print model

        # 2 - Construct a 2-way table
        # Table constructed from list of lists.
        # Rows: each term in the model
        # Cols: each subscript in the model
        rownames = []
        colnames = []
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