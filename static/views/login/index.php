<!DOCTYPE HTML>
<html lang="en">
    <head>
        <meta charset="utf-8"> 
        <title>Bixplorer</title>
        <link rel="stylesheet" type="text/css" href="<?php echo PUBLIC_PATH?>css/lib/bootstrap.min.css">
        <link rel="stylesheet" type="text/css" href="<?php echo PUBLIC_PATH?>css/lib/bootstrap-theme.min.css">    
        <link rel="stylesheet" type="text/css" href="<?php echo PUBLIC_PATH?>css/style.css">
        <script type="text/javascript" src="<?php echo PUBLIC_PATH?>js/lib/jquery-2.1.1.min.js"></script>
        <script type="text/javascript" src="<?php echo PUBLIC_PATH?>js/lib/bootstrap.min.js"></script>
    </head>

    <body>
        <div id="pheader">
            <h1>Bixplorer</h1>
            <h4>Visual Analytics for Intelligence Analysis with Biclusters</h4>
        </div>

        <div id="pbody" class="row">
            <div id="pslider" class="col-lg-9">
                <!-- slider for feature demonstration -->
                <div id="slider">
                    <div id="myCarousel" class="carousel slide" data-interval="3000" data-ride="carousel">
                        <!-- Carousel indicators -->
                        <ol class="carousel-indicators">
                            <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
                            <li data-target="#myCarousel" data-slide-to="1"></li>
                            <li data-target="#myCarousel" data-slide-to="2"></li>
                        </ol>
                        <!-- Carousel items -->
                        <div class="carousel-inner">
                            <div class="active item">
                                <img src="<?php echo PUBLIC_PATH?>imgs/bic1.png" class="img-rounded" alt="Rounded Image">
                                <div class="carousel-caption">
                                    <h3>Correlation Matrix</h3>
                                    <p>Coordinated relations between two domains</p>
                                </div>
                            </div>
                            <div class="item">
                                <img src="<?php echo PUBLIC_PATH?>imgs/bic2.png" class="img-rounded" alt="Rounded Image">
                                <div class="carousel-caption">
                                    <h3>Parallel Sets</h3>
                                    <p>Correlation across sets of entities</p>
                                </div>
                            </div>
                            <div class="item">
                                <img src="<?php echo PUBLIC_PATH?>imgs/bic3.png" class="img-rounded" alt="Rounded Image">
                                <div class="carousel-caption">
                                    <h3>Parallel Coordinates</h3>
                                    <p>Correlation across multiple dimensions</p>
                                </div>
                            </div>
                        </div>
                        <!-- Carousel nav -->
                        <a class="carousel-control left" href="#myCarousel" data-slide="prev">
                            <span class="glyphicon glyphicon-chevron-left"></span>
                        </a>
                        <a class="carousel-control right" href="#myCarousel" data-slide="next">
                            <span class="glyphicon glyphicon-chevron-right"></span>
                        </a>
                    </div>
                </div>
                
                <div id="discription">
                    <h5>Bixplorer is a visual analytics tool that supports intelligence analytsts to perform sensemaking tasks with bicusters.</h5>
                </div>
            </div>

            <div class="col-lg-3" id="pregister">
                <div id="rtab">
                   <div class="well well-lg">
                        <ul class="nav nav-tabs">
                            <li <?php if ($current_page == "login") { echo ' class="active" '; } ?>><a href="#login" data-toggle="tab">Login</a></li>
                            <li <?php if ($current_page == "register") { echo ' class="active" '; } ?>><a href="#create" data-toggle="tab">Sign up</a></li>
                        </ul>

                        <div id="myTabContent" class="tab-content">
                            <!-- login tab -->
                            <div class="tab-pane <?= $current_page == "login"?"active in":"fade"?>" id="login">
                                <form method="POST" action="<?= SERVER_PATH ?>login/login_action/">
                                    <fieldset>
                                        <div class="control-group">
                                            <!-- user name -->
                                            <div class="input-group">
                                                <span class="input-group-addon"><i class="glyphicon glyphicon-user"></i></span>
                                                <input id="login_username" type="text" class="form-control" name="username" value="<?php echo isset($login_username)?$login_username:""?>" placeholder="username" required>                                        
                                            </div>
                                        </div>                                  

                                        <div class="control-group">
                                            <!-- Password-->
                                            <div class="input-group">
                                                <span class="input-group-addon"><i class="glyphicon glyphicon-lock"></i></span>
                                                <input id="login_password" type="password" class="form-control" name="password" placeholder="password" required>
                                            </div>
                                        </div>

                                        <div class="control-group">
                                            <!-- Button -->
                                            <div class="controls">
    											<input id="login_submit" class="btn btn-success" type="submit" name="submit" value="Sign in" />
                                                <span class="pull-right" id="forgetPass"><a href="#">Forget password?</a></span>
                                            </div>
    										<!-- login error message -->
                                            <?php if(isset($login_feedback)){?>
    											<div id = "system_feedback">
    											<p style="color: red;"><?php echo $login_feedback;?></p>
    											</div>
    										<?php }?>
    										<!-- register success message -->
                                            <?php if(isset($register_success_info)){?>
    											<div id = "system_feedback">
    											<p style="color: green;"><?php echo $register_success_info;?></p>
    											</div>
    										<?php }?>
                                        </div>
                                    </fieldset>
                                </form>
                            </div>

                            <!-- register tab -->
                            <div class="tab-pane <?= $current_page == "register"?"active in":"fade"?>" id="create">
                                <form method="POST" action="<?= SERVER_PATH ?>login/register_action/">
                                    <fieldset>
                                        <div class="control-group">
                                            <!-- Username -->
                                            <div class="input-group">
                                                <span class="input-group-addon"><i class="glyphicon glyphicon-user"></i></span>
												<p class="username_message">
                                                    <a href="#" data-toggle="tooltip" class="message_tooltip">                                            
                                                        <input id="register_username" type="text" class="form-control" name="username" value="<?php echo isset($register_username)?$register_username:""?>" placeholder="username" required>                                       
                                                    </a>
                                                </p>
											</div>
                                        </div>

                                        <div class="control-group">
                                            <!-- Email -->
                                            <div class="input-group">
                                                <span class="input-group-addon"><i class="glyphicon glyphicon-envelope"></i></span>
                                                <p class="email_message">
                                                    <a href="#" data-toggle="tooltip" class="message_tooltip">                                            
                                                        <input id="register_email" type="text" class="form-control" name="email" value="<?php echo isset($register_email)?$register_email:""?>" placeholder="email" required>                                        
                                                    </a>
                                                </p>
                                            </div>
                                        </div>                               

                                       <div class="control-group">
                                            <!-- Password -->
                                            <div class="input-group">
                                                <span class="input-group-addon"><i class="glyphicon glyphicon-lock"></i></span>
                                                <p class="password1_message">
                                                    <a href="#" data-toggle="tooltip" class="message_tooltip">
                                                        <input id="register_password1" type="password" class="form-control" name="password1" placeholder="password" value="<?php "";//echo isset($password1)?$password1:""?>" required>
                                                    </a>
                                                </p>  
                                            </div>
                                        </div>

                                        <div class="control-group">
                                            <!-- Password again -->
                                            <div class="input-group">
                                                <span class="input-group-addon"><i class="glyphicon glyphicon-lock"></i></span>
                                                <p class="password2_message">
                                                    <a href="#" data-toggle="tooltip" class="message_tooltip">
                                                        <input id="register_password2" type="password" class="form-control" name="password2" placeholder="password again" value="<?php "";//echo isset($password2)?$password2:""?>" required>
                                                    </a>
                                                </p>
                                            </div>
                                        </div>

                                        <div class="control-group">
                                            <div class="controls">
    											<input id="register_submit" class="btn btn-primary" type="submit" name="submit" value="Sign up" disabled/>
                                            </div>
                                        </div>
                                        <!-- register error message -->
                                        <?php if(isset($register_feedback)){?>
    										<div id = "system_feedback">
    										<p style="color: red;"><?php echo $register_feedback;?></p>
    										</div>
    									<?php }?>
                                    </fieldset>
                                </form>
                            </div>
                        </div> <!-- end of tab content -->
                    </div>
                </div> <!-- end of rtab -->        
            </div>
        </div> <!-- end of pbody -->

        <script type="text/javascript" src="<?php echo PUBLIC_PATH?>js/regvalidate.js"></script>
    </body>
</html>