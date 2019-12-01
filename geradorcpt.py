"""
GERADOR CPTURBO
"""

from pandas import read_csv


def main():

    """
    Principal
    """

    dados_tabulados = read_csv('dados_tabulados.csv', sep='\t')
    qt_linhas = len(dados_tabulados)
    for linha in range(qt_linhas):
        titulo = capturar_info(dados_tabulados, linha, 'titulo')
        nome_do_autor = capturar_info(dados_tabulados, linha, 'nome_do_autor')
        link_da_capa = capturar_info(dados_tabulados, linha, 'link_da_capa')
        sinopse = capturar_info(dados_tabulados, linha, 'sinopse')
        idioma = capturar_info(dados_tabulados, linha, 'idioma')
        numero_de_paginas = capturar_info(dados_tabulados, linha,
                                          'numero_de_paginas')
        ano_de_lancamento = capturar_info(dados_tabulados, linha,
                                          'ano_de_lancamento')
        editora_genero = capturar_info(dados_tabulados, linha, 'editora_genero')
        formato_arquivo = capturar_info(dados_tabulados, linha,
                                        'formato_arquivo')
        tamanho_arquivo = capturar_info(dados_tabulados, linha,
                                        'tamanho_arquivo')
        tipo_compartilhamento = capturar_info(dados_tabulados, linha,
                                              'tipo_compartilhamento')
        link_de_download = capturar_info(dados_tabulados, linha,
                                         'link_de_download')

        # Encerrar script caso haja erro de captura
        if titulo is False:
            return
        if nome_do_autor is False:
            return
        if link_da_capa is False:
            return
        if sinopse is False:
            return
        if idioma is False:
            return
        if numero_de_paginas is False:
            return
        if ano_de_lancamento is False:
            return
        if editora_genero is False:
            return
        if formato_arquivo is False:
            return
        if tamanho_arquivo is False:
            return
        if tipo_compartilhamento is False:
            return
        if link_de_download is False:
            return

        html_codigo = secao08_m01(titulo, nome_do_autor, link_da_capa, sinopse,
                                  idioma, numero_de_paginas, ano_de_lancamento,
                                  editora_genero, formato_arquivo,
                                  tamanho_arquivo, tipo_compartilhamento,
                                  link_de_download)

        gerar_pagina_html(html_codigo, titulo, nome_do_autor)


def capturar_info(dataframe, numero_linha, nome_coluna):
    """
    Retorna a informação de uma coluna e linha informada.
    Retorna False me caso de erro na captura da informação
    :param dataframe: DataFrame. Dados tabulados.
    :param numero_linha: Integer. Número da linha.
    :param nome_coluna: String. Nome da coluna.
    :return: String. Informação procurada. | Boolean. Falso, em caso de erro.
    """

    try:
        informacao = dataframe.loc[numero_linha, nome_coluna]
        return informacao
    except:
        print(f'Erro ao capturar coluna "{nome_coluna}", linha {numero_linha}')
        return False


def secao08_m01(titulo, nome_do_autor, link_da_capa, sinopse, idioma,
                numero_de_paginas, ano_de_lancamento, editora_genero,
                formato_arquivo, tamanho_arquivo, tipo_compartilhamento,
                link_de_download):

    """
    Post de Ebook
    Gera o código html em String
    :return: String. Código HTML do post
    """

    html_codigo = f"""
        <table width="100%" align="center" border="0" 
            style="background-color:#d9e0ec !important; border-collapse:collapse; 
            border-spacing:0px; color:#333333; font-size:14px; text-align:start">
           <tbody>
              <tr valign="middle">
                 <td align="center" colspan="2" style="background-color:#6388c4; 
                    color:#ffffff; padding:5px">
                    <b><font size="5">
                        {titulo}
                    </font></b>
                    <br><font size="3"><b>
                        {nome_do_autor}
                    </b></font>
                 </td>
              </tr>
              <tr valign="middle">
                 <td align="center" colspan="2"><br></td>
              </tr>
              <tr valign="middle">
                 <td align="center" style="background-color:#6388c4; color:#ffffff; 
                    padding:5px">Capa</td>
                 <td align="center" style="background-color:#6388c4; color:#ffffff; 
                    padding:5px">Sinopse</td>
              </tr>
              <tr valign="middle">
                 <td valign="top" width="50%" style="padding:15px">
                    <div style="text-align:center">
                    <img data-cke-saved-src="
                        {link_da_capa}
                    " src="
                        {link_da_capa}
                    " style="border:0px; text-align:center; 
                        vertical-align:middle"></div>
                 </td>
                 <td valign="top" width="50%" style="padding:15px">
                    <div style="text-align:justify">
                        {sinopse}
                    </div>
                 </td>
              </tr>
              <tr valign="middle">
                 <td align="center" style="background-color:#6388c4; color:#ffffff; 
                    padding:5px">
                    <div>Dados do Curso</div>
                 </td>
                 <td align="center" style="background-color:#6388c4; color:#ffffff; 
                    padding:5px">
                    <div>Dados do Arquivo</div>
                 </td>
              </tr>
              <tr valign="middle">
                 <td valign="top" width="50%" style="padding:15px">
                    <b>Idioma:</b><span>&nbsp;</span>
                        {idioma}
                    <br>
                    <b>Quantidade de páginas:</b><span>&nbsp;</span>
                        {numero_de_paginas}
                    <br>
                    <b>Ano de Lançamento:</b><span>&nbsp;</span>
                        {ano_de_lancamento}
                    <br>
                    <b>Editora/Gênero:</b><span>&nbsp;</span>
                        {editora_genero}
                 </td>
                 <td valign="top" width="50%" style="padding:15px">
                    <b>Formato do Arquivo:</b><span>&nbsp;</span>
                        {formato_arquivo}
                    <br>
                    <b>Tamanho do Arquivo:</b><span>&nbsp;</span>
                        {tamanho_arquivo}
                    <br>
                    <b>Tipo de Compartilhamento:</b><span>&nbsp;</span>
                        {tipo_compartilhamento}
                 </td>
              </tr>
              <tr valign="middle">
                 <td align="center" colspan="2" style="background-color:#6388c4; 
                    color:#ffffff; padding:5px">Downloadtd>
              </tr>
              <tr valign="middle">
                 <td align="center" colspan="2"><br>
                    [code]
                        {link_de_download}
                    [/code]
                </td>
              </tr>
           </tbody>
        </table>
        """

    return html_codigo


def gerar_pagina_html(html_codigo, titulo, nome_do_autor):
    """
    Gera post em formato .html a partir do código html em String
    :param html_codigo: String. Página HTML do post
    """

    nome_arquivo = f'{titulo}-{nome_do_autor}.html'
    file = open(nome_arquivo, 'w')
    file.write(html_codigo)
    file.close()

    print(f'Post Gerado em .html: {titulo}-{nome_do_autor}')


main()