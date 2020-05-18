:orphan:

============
セットアップ
============
これはこのドキュメント作成に関するメモ。
Pythonでリモートセンシングを行う上では不要。

Anaconda
============
Anacondaで環境構築しておく。

jupyter notebook
================

インストール
------------
下記に従いインストールを行う。
https://jupyter.org/install

.. code-block:: bash

    $ conda install -c conda-forge jupyterlab


Sphinx
============

インストール
------------
下記に従い、インストールを行う。
https://www.sphinx-doc.org/en/master/usage/installation.html


.. code-block:: bash

    $ sudo apt install python3-sphinx

nbsphinx
============

インストール
------------
下記に従い、インストールを行う。
https://nbsphinx.readthedocs.io/en/latest/installation.html

.. code-block:: bash

    $ conda activate py37
    $ conda install -c conda-forge nbsphinx

また、下記のインストールをしておく。

.. code-block:: bash

   $ conda install -c conda-forge pandoc
   $ conda install -c conda-forge ipython


セットアップ
------------

``sphinx.cmd.quickstart`` で、セットアップを行う。

.. code-block:: bash

   $ python3 -m sphinx.cmd.quickstart

使用した設定は以下。

.. code-block:: bash

    > Separate source and build directories (y/n) [n]: y
    > Project name: rs-with-python
    > Author name(s): Taka
    > Project release []:
    > Project language [en]: ja

下記のようなディレクトリが作成される。 ::

    .
    ├── build
    ├── make.bat
    ├── Makefile
    └── source
        ├── conf.py
        ├── index.rst
        ├── _static
        └── _templates

``read-the-doc`` スタイルを適用するため、以下を実行。

.. code-block:: bash

   conda install sphinx_rtd_theme

``source/conf.py`` を以下のように修正

.. code-block:: python

   import sphinx_rtd_theme  # この行を追記する。

   ...

   extensions = [
      'nbsphinx',
      'sphinx.ext.mathjax',
      'sphinx.ext.githubpages',
      'sphinx_rtd_theme'
   ]

   html_theme = "sphinx_rtd_theme"

Github Pagesでの公開設定
========================

ビルド
----------------------
``Makefile`` ファイルを以下のとおり変更

.. literalinclude:: ../Makefile


``$ make html`` を実行する。

下記のようにhtmlディレクトリが作成される。::

    .
    ├── docs
    │   ├── doctrees
    │   │   ├── environment.pickle
    │   │   └── index.doctree
    │   └── html
    │       ├── genindex.html
    │       ├── index.html
    │       ├── objects.inv
    │       ├── search.html
    │       ├── searchindex.js
    │       ├── _sources
    │       │   └── index.rst.txt
    │       └── _static
    │           ├── alabaster.css
    │           ├── basic.css
    │           ├── custom.css
    │           ├── doctools.js
    │           ├── documentation_options.js
    │           ├── file.png
    │           ├── jquery-3.4.1.js
    │           ├── jquery.js
    │           ├── language_data.js
    │           ├── minus.png
    │           ├── plus.png
    │           ├── pygments.css
    │           ├── searchtools.js
    │           ├── translations.js
    │           ├── underscore-1.3.1.js
    │           └── underscore.js
    ├── make.bat
    ├── Makefile
    └── source
        ├── conf.py
        ├── index.rst
        ├── _static
        └── _templates


Git, Githubの設定
----------------------

githubのリポジトリを作成、 ``gitinit`` の実行、ルートディレクトリに
``.gitignore`` を保存。

コンテンツの追加・更新
======================
追加
----------------------
``.rst`` ファイル
^^^^^^^^^^^^^^^^^
1. ``source`` ディレクトリ内に ``.rst`` ファイルを追加する。
2. ``index.rst`` に追加したファイル名(拡張子を除く)を追記する。
3. ``make html`` を実行する。

``.ipynb`` ファイル
^^^^^^^^^^^^^^^^^^^
1. ``source`` ディレクトリ内に ``.ipynb`` ファイルを追加する。
2. ``index.rst`` に追加したファイル名(拡張子を除く)を追記する。
3. ``make html`` を実行する。

更新
----------------------
``source`` ディレクトリ内のファイルを変更する。
``make html`` を実行する。

