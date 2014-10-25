<!doctype html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <title>Bixplorer</title>
    <link rel="stylesheet" type="text/css" href="<?php echo PUBLIC_PATH?>css/lib/bootstrap.min.css" />
    <link rel="stylesheet" type="text/css" href="<?php echo PUBLIC_PATH?>css/lib/bootstrap-select.min.css" />
    <link rel="stylesheet" type="text/css" href="<?php echo PUBLIC_PATH?>css/lib/bootcards-desktop.min.css" />    
    <link rel="stylesheet" type="text/css" href="<?php echo PUBLIC_PATH?>css/lib/jquery.dataTables.min.css" />
    <link rel="stylesheet" type="text/css" href="<?php echo PUBLIC_PATH?>css/style.css" />
	<script type="text/javascript" src="<?php echo PUBLIC_PATH?>js/lib/jquery-2.1.1.min.js"></script>
    <script type="text/javascript" src="<?php echo PUBLIC_PATH?>js/lib/jquery.form.js"></script>
    <script type="text/javascript" src="<?php echo PUBLIC_PATH?>js/lib/bootstrap.min.js"></script>
    <script type="text/javascript" src="<?php echo PUBLIC_PATH?>js/lib/bootstrap-select.min.js"></script>
	<script type="text/javascript">window.PUBLIC_PATH = "<?php echo PUBLIC_PATH?>";</script>
	<script type="text/javascript">window.SERVER_PATH = "<?php echo SERVER_PATH?>";</script>
</head>

<body class="db_after_login">

    <!-- top navigation bar -->
    <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container-fluid">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target=".navbar-collapse">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="<?php echo SERVER_PATH.'home/index/'?>">Bixplorer</a>
            </div>
            
            <div class="navbar-collapse collapse">
                <ul class="nav navbar-nav navbar-right">
                    <!-- home menu -->
                    <li class="<?php if(isset($current_tab)){
                        if($current_tab == 'home') echo "active";
                    }?>"><a href="<?php echo SERVER_PATH.'home/index/'?>"><span class="glyphicon glyphicon-home"></span> Home</a></li>
                    
                    <!-- project management menu -->
                    <li class="dropdown <?php if(isset($current_tab)){
    					if($current_tab == 'project') echo "active";
    				}?>">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown"><span class="glyphicon glyphicon-tasks"></span> Project Management <span class="caret"></span></a>
                        <ul class="dropdown-menu" role="menu">
                            <li><a href="<?php echo SERVER_PATH.'project/add/'?>"><span class="glyphicon glyphicon-plus"></span> Create a new project</a></li>
                            <li><a href="<?php echo SERVER_PATH.'project/plist/'?>"><span class="glyphicon glyphicon-list"></span> My project list</a></li>
                        </ul>
                    </li>
                    
                    <!-- dataset management menu -->
                    <li class="dropdown <?php if(isset($current_tab)){
    					if($current_tab == 'dataset') echo "active";
    				}?>"><a href="<?php echo SERVER_PATH.'dataset/index/'?>"><span class="glyphicon glyphicon-cog"></span> Dataset Management</a></li>
                    
                    <!-- analytics workspace menu -->
                    <li class="dropdown <?php if(isset($current_tab)){
    					if($current_tab == 'dataviz') echo "active";
    				}?>"><a href="<?php echo SERVER_PATH.'dataviz/index/'?>"><span class="glyphicon glyphicon-eye-open"></span> Analytical Workspace</a></li>
                    
                    <!-- profile menu -->
                    <li class="<?php if(isset($current_tab)){
                        if($current_tab == 'profile') echo "active";
                    }?>"><a href="<?php echo SERVER_PATH.'login/profile/'?>"><span class="glyphicon glyphicon-user"></span> My Profile</a></li>                
                    
                    <!-- about menu -->
                    <li class="dropdown <?php if(isset($current_tab)){
    					if($current_tab == 'about') echo "active";
    				}?>"><a href="<?php echo SERVER_PATH.'home/about/'?>"><span class="glyphicon glyphicon-info-sign"></span> About</a></li>
                    
                    <!-- logout menu -->
                    <li><a href="<?php echo SERVER_PATH.'login/logout_action/'?>"><span class="glyphicon glyphicon-log-out"></span> Logout</a></li>            
                </ul>
            </div>
        </div>
    </div>