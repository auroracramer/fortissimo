  


<!DOCTYPE html>
<html>
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# githubog: http://ogp.me/ns/fb/githubog#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>CS164-Class-Interpreter/util.py at master · hjjiang/CS164-Class-Interpreter · GitHub</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png" />
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png" />
    <link rel="logo" type="image/svg" href="http://github-media-downloads.s3.amazonaws.com/github-logo.svg" />
    <link rel="xhr-socket" href="/_sockets">
    <meta name="msapplication-TileImage" content="/windows-tile.png">
    <meta name="msapplication-TileColor" content="#ffffff">

    
    
    <link rel="icon" type="image/x-icon" href="/favicon.ico" />

    <meta content="authenticity_token" name="csrf-param" />
<meta content="QRwdnPBA5vCRnq9np0t8fsPsmeCSMR5m/pjA6l/Qqn4=" name="csrf-token" />

    <link href="https://a248.e.akamai.net/assets.github.com/assets/github-21d1f919c9b16786238504ad1232b4937bbdd088.css" media="all" rel="stylesheet" type="text/css" />
    <link href="https://a248.e.akamai.net/assets.github.com/assets/github2-b702f2bd3370655be3cd89c1cd8cb00052d6a475.css" media="all" rel="stylesheet" type="text/css" />
    


      <script src="https://a248.e.akamai.net/assets.github.com/assets/frameworks-92d138f450f2960501e28397a2f63b0f100590f0.js" type="text/javascript"></script>
      <script src="https://a248.e.akamai.net/assets.github.com/assets/github-8b597885ade82d6a3d9108d93ea8e86b9f294d91.js" type="text/javascript"></script>
      
      <meta http-equiv="x-pjax-version" content="77a530946004f4df817ad3a299a913ed">

        <link data-pjax-transient rel='permalink' href='/hjjiang/CS164-Class-Interpreter/blob/e549b9d1d5d388e3a51a42feb1df46f36ff5e14f/util.py'>
    <meta property="og:title" content="CS164-Class-Interpreter"/>
    <meta property="og:type" content="githubog:gitrepository"/>
    <meta property="og:url" content="https://github.com/hjjiang/CS164-Class-Interpreter"/>
    <meta property="og:image" content="https://secure.gravatar.com/avatar/63c7d91916085620456f3bc721923008?s=420&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png"/>
    <meta property="og:site_name" content="GitHub"/>
    <meta property="og:description" content="CS164-Class-Interpreter - CS164 Class Interpreter"/>
    <meta property="twitter:card" content="summary"/>
    <meta property="twitter:site" content="@GitHub">
    <meta property="twitter:title" content="hjjiang/CS164-Class-Interpreter"/>

    <meta name="description" content="CS164-Class-Interpreter - CS164 Class Interpreter" />

  <link href="https://github.com/hjjiang/CS164-Class-Interpreter/commits/master.atom" rel="alternate" title="Recent Commits to CS164-Class-Interpreter:master" type="application/atom+xml" />

  </head>


  <body class="logged_out page-blob linux vis-public env-production  ">
    <div id="wrapper">

      

      
      
      

      
      <div class="header header-logged-out">
  <div class="container clearfix">

      <a class="header-logo-wordmark" href="https://github.com/">Github</a>

    <div class="header-actions">
        <a class="button primary" href="https://github.com/signup">Sign up for free</a>
      <a class="button" href="https://github.com/login?return_to=%2Fhjjiang%2FCS164-Class-Interpreter%2Fblob%2Fmaster%2Futil.py">Sign in</a>
    </div>

      <ul class="top-nav">
          <li class="explore"><a href="https://github.com/explore">Explore GitHub</a></li>
        <li class="search"><a href="https://github.com/search">Search</a></li>
        <li class="features"><a href="https://github.com/features">Features</a></li>
          <li class="blog"><a href="https://github.com/blog">Blog</a></li>
      </ul>

  </div>
</div>


      

      


            <div class="site hfeed" itemscope itemtype="http://schema.org/WebPage">
      <div class="hentry">
        
        <div class="pagehead repohead instapaper_ignore readability-menu ">
          <div class="container">
            <div class="title-actions-bar">
              

<ul class="pagehead-actions">



    <li>
      <a href="/login?return_to=%2Fhjjiang%2FCS164-Class-Interpreter"
        class="minibutton js-toggler-target star-button entice tooltipped upwards"
        title="You must be signed in to use this feature" rel="nofollow">
        <span class="mini-icon mini-icon-star"></span>Star
      </a>
      <a class="social-count js-social-count" href="/hjjiang/CS164-Class-Interpreter/stargazers">
        2
      </a>
    </li>
    <li>
      <a href="/login?return_to=%2Fhjjiang%2FCS164-Class-Interpreter"
        class="minibutton js-toggler-target fork-button entice tooltipped upwards"
        title="You must be signed in to fork a repository" rel="nofollow">
        <span class="mini-icon mini-icon-fork"></span>Fork
      </a>
      <a href="/hjjiang/CS164-Class-Interpreter/network" class="social-count">
        0
      </a>
    </li>
</ul>

              <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
                <span class="repo-label"><span>public</span></span>
                <span class="mega-icon mega-icon-public-repo"></span>
                <span class="author vcard">
                  <a href="/hjjiang" class="url fn" itemprop="url" rel="author">
                  <span itemprop="title">hjjiang</span>
                  </a></span> /
                <strong><a href="/hjjiang/CS164-Class-Interpreter" class="js-current-repository">CS164-Class-Interpreter</a></strong>
              </h1>
            </div>

            
  <ul class="tabs">
    <li class="pulse-nav"><a href="/hjjiang/CS164-Class-Interpreter/pulse" highlight="pulse" rel="nofollow"><span class="mini-icon mini-icon-pulse"></span></a></li>
    <li><a href="/hjjiang/CS164-Class-Interpreter" class="selected" highlight="repo_source repo_downloads repo_commits repo_tags repo_branches">Code</a></li>
    <li><a href="/hjjiang/CS164-Class-Interpreter/network" highlight="repo_network">Network</a></li>
    <li><a href="/hjjiang/CS164-Class-Interpreter/pulls" highlight="repo_pulls">Pull Requests <span class='counter'>0</span></a></li>

      <li><a href="/hjjiang/CS164-Class-Interpreter/issues" highlight="repo_issues">Issues <span class='counter'>0</span></a></li>



    <li><a href="/hjjiang/CS164-Class-Interpreter/graphs" highlight="repo_graphs repo_contributors">Graphs</a></li>


  </ul>
  
<div class="tabnav">

  <span class="tabnav-right">
    <ul class="tabnav-tabs">
          <li><a href="/hjjiang/CS164-Class-Interpreter/tags" class="tabnav-tab" highlight="repo_tags">Tags <span class="counter blank">0</span></a></li>
    </ul>
    
  </span>

  <div class="tabnav-widget scope">


    <div class="select-menu js-menu-container js-select-menu js-branch-menu">
      <a class="minibutton select-menu-button js-menu-target" data-hotkey="w" data-ref="master">
        <span class="mini-icon mini-icon-branch"></span>
        <i>branch:</i>
        <span class="js-select-button">master</span>
      </a>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container">

        <div class="select-menu-modal">
          <div class="select-menu-header">
            <span class="select-menu-title">Switch branches/tags</span>
            <span class="mini-icon mini-icon-remove-close js-menu-close"></span>
          </div> <!-- /.select-menu-header -->

          <div class="select-menu-filters">
            <div class="select-menu-text-filter">
              <input type="text" id="commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
            </div>
            <div class="select-menu-tabs">
              <ul>
                <li class="select-menu-tab">
                  <a href="#" data-tab-filter="branches" class="js-select-menu-tab">Branches</a>
                </li>
                <li class="select-menu-tab">
                  <a href="#" data-tab-filter="tags" class="js-select-menu-tab">Tags</a>
                </li>
              </ul>
            </div><!-- /.select-menu-tabs -->
          </div><!-- /.select-menu-filters -->

          <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket css-truncate" data-tab-filter="branches">

            <div data-filterable-for="commitish-filter-field" data-filterable-type="substring">

                <div class="select-menu-item js-navigation-item selected">
                  <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                  <a href="/hjjiang/CS164-Class-Interpreter/blob/master/util.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="master" rel="nofollow" title="master">master</a>
                </div> <!-- /.select-menu-item -->
            </div>

              <div class="select-menu-no-results">Nothing to show</div>
          </div> <!-- /.select-menu-list -->


          <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket css-truncate" data-tab-filter="tags">
            <div data-filterable-for="commitish-filter-field" data-filterable-type="substring">

            </div>

            <div class="select-menu-no-results">Nothing to show</div>

          </div> <!-- /.select-menu-list -->

        </div> <!-- /.select-menu-modal -->
      </div> <!-- /.select-menu-modal-holder -->
    </div> <!-- /.select-menu -->

  </div> <!-- /.scope -->

  <ul class="tabnav-tabs">
    <li><a href="/hjjiang/CS164-Class-Interpreter" class="selected tabnav-tab" highlight="repo_source">Files</a></li>
    <li><a href="/hjjiang/CS164-Class-Interpreter/commits/master" class="tabnav-tab" highlight="repo_commits">Commits</a></li>
    <li><a href="/hjjiang/CS164-Class-Interpreter/branches" class="tabnav-tab" highlight="repo_branches" rel="nofollow">Branches <span class="counter ">1</span></a></li>
  </ul>

</div>

  
  
  


            
          </div>
        </div><!-- /.repohead -->

        <div id="js-repo-pjax-container" class="container context-loader-container" data-pjax-container>
          


<!-- blob contrib key: blob_contributors:v21:3b7d04ceca58cd121877c4c2048e0672 -->
<!-- blob contrib frag key: views10/v8/blob_contributors:v21:3b7d04ceca58cd121877c4c2048e0672 -->


<div id="slider">
    <div class="frame-meta">

      <p title="This is a placeholder element" class="js-history-link-replace hidden"></p>

        <div class="breadcrumb">
          <span class='bold'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/hjjiang/CS164-Class-Interpreter" class="js-slide-to" data-branch="master" data-direction="back" itemscope="url"><span itemprop="title">CS164-Class-Interpreter</span></a></span></span><span class="separator"> / </span><strong class="final-path">util.py</strong> <span class="js-zeroclipboard zeroclipboard-button" data-clipboard-text="util.py" data-copied-hint="copied!" title="copy to clipboard"><span class="mini-icon mini-icon-clipboard"></span></span>
        </div>

      <a href="/hjjiang/CS164-Class-Interpreter/find/master" class="js-slide-to" data-hotkey="t" style="display:none">Show File Finder</a>


        <div class="commit commit-loader file-history-tease js-deferred-content" data-url="/hjjiang/CS164-Class-Interpreter/contributors/master/util.py">
          Fetching contributors…

          <div class="participation">
            <p class="loader-loading"><img alt="Octocat-spinner-32-eaf2f5" height="16" src="https://a248.e.akamai.net/assets.github.com/images/spinners/octocat-spinner-32-EAF2F5.gif?1338956357" width="16" /></p>
            <p class="loader-error">Cannot retrieve contributors at this time</p>
          </div>
        </div>

    </div><!-- ./.frame-meta -->

    <div class="frames">
      <div class="frame" data-permalink-url="/hjjiang/CS164-Class-Interpreter/blob/e549b9d1d5d388e3a51a42feb1df46f36ff5e14f/util.py" data-title="CS164-Class-Interpreter/util.py at master · hjjiang/CS164-Class-Interpreter · GitHub" data-type="blob">

        <div id="files" class="bubble">
          <div class="file">
            <div class="meta">
              <div class="info">
                <span class="icon"><b class="mini-icon mini-icon-text-file"></b></span>
                <span class="mode" title="File Mode">file</span>
                  <span>47 lines (37 sloc)</span>
                <span>1.193 kb</span>
              </div>
              <div class="actions">
                <div class="button-group">
                      <a class="minibutton js-entice" href=""
                         data-entice="You must be signed in and on a branch to make or propose changes">Edit</a>
                  <a href="/hjjiang/CS164-Class-Interpreter/raw/master/util.py" class="button minibutton " id="raw-url">Raw</a>
                    <a href="/hjjiang/CS164-Class-Interpreter/blame/master/util.py" class="button minibutton ">Blame</a>
                  <a href="/hjjiang/CS164-Class-Interpreter/commits/master/util.py" class="button minibutton " rel="nofollow">History</a>
                </div><!-- /.button-group -->
              </div><!-- /.actions -->

            </div>
                <div class="blob-wrapper data type-python js-blob-data">
      <table class="file-code file-diff">
        <tr class="file-code-line">
          <td class="blob-line-nums">
            <span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
<span id="L43" rel="#L43">43</span>
<span id="L44" rel="#L44">44</span>
<span id="L45" rel="#L45">45</span>
<span id="L46" rel="#L46">46</span>

          </td>
          <td class="blob-line-code">
                  <div class="highlight"><pre><div class='line' id='LC1'><span class="kn">import</span> <span class="nn">sys</span></div><div class='line' id='LC2'><br/></div><div class='line' id='LC3'><span class="k">class</span> <span class="nc">Ambiguous</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span></div><div class='line' id='LC4'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">value</span><span class="p">):</span></div><div class='line' id='LC5'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">value</span></div><div class='line' id='LC6'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC7'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">repr</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">value</span><span class="p">)</span></div><div class='line' id='LC8'><br/></div><div class='line' id='LC9'><span class="k">def</span> <span class="nf">doImports</span> <span class="p">(</span><span class="n">moduleNames</span><span class="p">):</span></div><div class='line' id='LC10'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;Imports the modules named in the sequence MODULES into a new global</span></div><div class='line' id='LC11'><span class="sd">    object (dictionary).</span></div><div class='line' id='LC12'><span class="sd">    Returns the new global object.</span></div><div class='line' id='LC13'><span class="sd">    &#39;&#39;&#39;</span></div><div class='line' id='LC14'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">glob</span> <span class="o">=</span> <span class="p">{}</span></div><div class='line' id='LC15'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">module</span> <span class="ow">in</span> <span class="n">moduleNames</span><span class="p">:</span></div><div class='line' id='LC16'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">exec</span> <span class="p">(</span><span class="s">&#39;import </span><span class="si">%s</span><span class="s">&#39;</span><span class="o">%</span> <span class="p">(</span><span class="n">module</span><span class="p">),</span> <span class="n">glob</span><span class="p">)</span></div><div class='line' id='LC17'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">glob</span></div><div class='line' id='LC18'><br/></div><div class='line' id='LC19'><br/></div><div class='line' id='LC20'><span class="k">def</span> <span class="nf">createFunction</span> <span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">args</span><span class="p">,</span> <span class="n">code</span><span class="p">,</span> <span class="n">env</span><span class="p">):</span></div><div class='line' id='LC21'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;Create and return the function NAME.</span></div><div class='line' id='LC22'><span class="sd">    NAME, ARGS, and CODE represent the function signature and body.  ENV</span></div><div class='line' id='LC23'><span class="sd">    is the environment in which to define the function NAME.</span></div><div class='line' id='LC24'><br/></div><div class='line' id='LC25'><span class="sd">    The function will be created as:</span></div><div class='line' id='LC26'><span class="sd">      def NAME (arg0, arg1, ...): CODE</span></div><div class='line' id='LC27'><span class="sd">    &#39;&#39;&#39;</span></div><div class='line' id='LC28'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">strArgs</span> <span class="o">=</span> <span class="s">&#39;,&#39;</span><span class="o">.</span><span class="n">join</span> <span class="p">(</span><span class="n">args</span><span class="p">)</span></div><div class='line' id='LC29'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">exec</span> <span class="p">(</span><span class="s">&#39;def </span><span class="si">%s</span><span class="s">(</span><span class="si">%s</span><span class="s">):</span><span class="si">%s</span><span class="s">&#39;</span><span class="o">%</span> <span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">strArgs</span><span class="p">,</span> <span class="n">code</span><span class="p">),</span> <span class="n">env</span><span class="p">)</span></div><div class='line' id='LC30'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">env</span><span class="p">[</span><span class="n">name</span><span class="p">]</span></div><div class='line' id='LC31'><br/></div><div class='line' id='LC32'><br/></div><div class='line' id='LC33'><span class="n">_nextNum</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC34'><span class="k">def</span> <span class="nf">uniqueIdentifier</span> <span class="p">():</span></div><div class='line' id='LC35'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;Return an identifier that has never before been returned by</span></div><div class='line' id='LC36'><span class="sd">    uniqueIdentifier ().</span></div><div class='line' id='LC37'><span class="sd">    &#39;&#39;&#39;</span></div><div class='line' id='LC38'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">global</span> <span class="n">_nextNum</span></div><div class='line' id='LC39'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">_nextNum</span> <span class="o">+=</span> <span class="mi">1</span></div><div class='line' id='LC40'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="s">&#39;f</span><span class="si">%d</span><span class="s">&#39;</span><span class="o">%</span><span class="p">(</span><span class="n">_nextNum</span><span class="p">)</span></div><div class='line' id='LC41'><br/></div><div class='line' id='LC42'><br/></div><div class='line' id='LC43'><span class="k">def</span> <span class="nf">error</span> <span class="p">(</span><span class="n">message</span><span class="p">):</span></div><div class='line' id='LC44'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;Print MESSAGE to stderr and raise SyntaxError&#39;&#39;&#39;</span></div><div class='line' id='LC45'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="o">&gt;&gt;</span><span class="n">sys</span><span class="o">.</span><span class="n">stderr</span><span class="p">,</span> <span class="n">message</span></div><div class='line' id='LC46'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="ne">SyntaxError</span><span class="p">(</span><span class="s">&#39;Error&#39;</span><span class="p">)</span></div></pre></div>
          </td>
        </tr>
      </table>
  </div>

          </div>
        </div>

        <a href="#jump-to-line" rel="facebox" data-hotkey="l" class="js-jump-to-line" style="display:none">Jump to Line</a>
        <div id="jump-to-line" style="display:none">
          <h2>Jump to Line</h2>
          <form accept-charset="UTF-8" class="js-jump-to-line-form">
            <input class="textfield js-jump-to-line-field" type="text">
            <div class="full-button">
              <button type="submit" class="button">Go</button>
            </div>
          </form>
        </div>

      </div>
    </div>
</div>

<div id="js-frame-loading-template" class="frame frame-loading large-loading-area" style="display:none;">
  <img class="js-frame-loading-spinner" src="https://a248.e.akamai.net/assets.github.com/images/spinners/octocat-spinner-128.gif?1347543528" height="64" width="64">
</div>


        </div>
      </div>
      <div class="context-overlay"></div>
    </div>

      <div id="footer-push"></div><!-- hack for sticky footer -->
    </div><!-- end of wrapper - hack for sticky footer -->

      <!-- footer -->
      <div id="footer">
  <div class="container clearfix">

      <dl class="footer_nav">
        <dt>GitHub</dt>
        <dd><a href="https://github.com/about">About us</a></dd>
        <dd><a href="https://github.com/blog">Blog</a></dd>
        <dd><a href="https://github.com/contact">Contact &amp; support</a></dd>
        <dd><a href="http://enterprise.github.com/">GitHub Enterprise</a></dd>
        <dd><a href="http://status.github.com/">Site status</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Applications</dt>
        <dd><a href="http://mac.github.com/">GitHub for Mac</a></dd>
        <dd><a href="http://windows.github.com/">GitHub for Windows</a></dd>
        <dd><a href="http://eclipse.github.com/">GitHub for Eclipse</a></dd>
        <dd><a href="http://mobile.github.com/">GitHub mobile apps</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Services</dt>
        <dd><a href="http://get.gaug.es/">Gauges: Web analytics</a></dd>
        <dd><a href="http://speakerdeck.com">Speaker Deck: Presentations</a></dd>
        <dd><a href="https://gist.github.com">Gist: Code snippets</a></dd>
        <dd><a href="http://jobs.github.com/">Job board</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Documentation</dt>
        <dd><a href="http://help.github.com/">GitHub Help</a></dd>
        <dd><a href="http://developer.github.com/">Developer API</a></dd>
        <dd><a href="http://github.github.com/github-flavored-markdown/">GitHub Flavored Markdown</a></dd>
        <dd><a href="http://pages.github.com/">GitHub Pages</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>More</dt>
        <dd><a href="http://training.github.com/">Training</a></dd>
        <dd><a href="https://github.com/edu">Students &amp; teachers</a></dd>
        <dd><a href="http://shop.github.com">The Shop</a></dd>
        <dd><a href="/plans">Plans &amp; pricing</a></dd>
        <dd><a href="http://octodex.github.com/">The Octodex</a></dd>
      </dl>

      <hr class="footer-divider">


    <p class="right">&copy; 2013 <span title="0.07553s from fe1.rs.github.com">GitHub</span>, Inc. All rights reserved.</p>
    <a class="left" href="https://github.com/">
      <span class="mega-icon mega-icon-invertocat"></span>
    </a>
    <ul id="legal">
        <li><a href="https://github.com/site/terms">Terms of Service</a></li>
        <li><a href="https://github.com/site/privacy">Privacy</a></li>
        <li><a href="https://github.com/security">Security</a></li>
    </ul>

  </div><!-- /.container -->

</div><!-- /.#footer -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-fullscreen-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="js-fullscreen-contents" placeholder="" data-suggester="fullscreen_suggester"></textarea>
          <div class="suggester-container">
              <div class="suggester fullscreen-suggester js-navigation-container" id="fullscreen_suggester"
                 data-url="/hjjiang/CS164-Class-Interpreter/suggestions/commit">
              </div>
          </div>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped leftwards" title="Exit Zen Mode">
      <span class="mega-icon mega-icon-normalscreen"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped leftwards"
      title="Switch themes">
      <span class="mini-icon mini-icon-brightness"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="mini-icon mini-icon-exclamation"></span>
      Something went wrong with that request. Please try again.
      <a href="#" class="mini-icon mini-icon-remove-close ajax-error-dismiss"></a>
    </div>

    
    
    <span id='server_response_time' data-time='0.07596' data-host='fe1'></span>
    
  </body>
</html>

